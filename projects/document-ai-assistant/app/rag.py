import os
from pathlib import Path

import chromadb
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
from openai import OpenAI
from pypdf import PdfReader

CHROMA_DIR = os.getenv("CHROMA_PERSIST_DIR", "./data/chroma")
COLLECTION_NAME = "portfolio_docs"

CHUNK_SIZE = 800
CHUNK_OVERLAP = 120


def _client() -> OpenAI:
    return OpenAI(
        api_key=os.environ["OPENAI_API_KEY"],
        base_url=os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1"),
    )


def _collection():
    Path(CHROMA_DIR).mkdir(parents=True, exist_ok=True)
    embed = OpenAIEmbeddingFunction(
        api_key=os.environ["OPENAI_API_KEY"],
        api_base=os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1"),
        model_name=os.getenv("EMBEDDING_MODEL", "text-embedding-3-small"),
    )
    db = chromadb.PersistentClient(path=CHROMA_DIR)
    return db.get_or_create_collection(name=COLLECTION_NAME, embedding_function=embed)


def _chunk_text(text: str) -> list[str]:
    text = " ".join(text.split())
    if not text:
        return []
    chunks: list[str] = []
    start = 0
    while start < len(text):
        end = start + CHUNK_SIZE
        chunks.append(text[start:end])
        start = end - CHUNK_OVERLAP
    return chunks


def ingest_pdf(pdf_path: Path, doc_id: str) -> int:
    reader = PdfReader(str(pdf_path))
    pages = [p.extract_text() or "" for p in reader.pages]
    full_text = "\n".join(pages)
    chunks = _chunk_text(full_text)
    if not chunks:
        return 0

    coll = _collection()
    ids = [f"{doc_id}_{i}" for i in range(len(chunks))]
    metadatas = [{"doc_id": doc_id, "source": pdf_path.name, "chunk": i} for i in range(len(chunks))]
    coll.add(documents=chunks, ids=ids, metadatas=metadatas)
    return len(chunks)


def chat_with_documents(question: str, top_k: int = 4) -> tuple[str, list[str]]:
    coll = _collection()
    if coll.count() == 0:
        return (
            "No documents indexed yet. Upload a PDF via POST /documents/upload first.",
            [],
        )

    results = coll.query(query_texts=[question], n_results=top_k)
    docs = results.get("documents", [[]])[0]
    metas = results.get("metadatas", [[]])[0]

    context = "\n\n---\n\n".join(docs)
    sources = sorted({m.get("source", "unknown") for m in metas})

    client = _client()
    model = os.getenv("CHAT_MODEL", "gpt-4o-mini")
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": (
                    "You answer only from the provided context. "
                    "If the answer is not in the context, say you don't know."
                ),
            },
            {
                "role": "user",
                "content": f"Context:\n{context}\n\nQuestion: {question}",
            },
        ],
        temperature=0.2,
    )
    answer = completion.choices[0].message.content or ""
    return answer, sources
