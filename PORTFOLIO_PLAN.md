# Portfolio build plan (6–8 weeks)

Goal: **3 public GitHub projects** with READMEs, screenshots, and at least **one live URL** (even a small EC2 instance) before heavy job applications.

## Principles

- Do not copy NIELIT proprietary code — rebuild **small, honest demos** of patterns you already know.
- Add skills to your CV only after they appear in a committed project.
- Every project needs: `README.md`, `.env.example`, `Dockerfile`, and 2–3 screenshots.

---

## Phase 1 — GitHub presence (Week 1)

| Task | Done |
|------|------|
| Push this repo to GitHub | ☐ |
| Profile README: headline + links to these repos | ☐ |
| LinkedIn headline matches CV: *Software Developer \| PHP, Node.js, React \| Cloud & AI* | ☐ |
| Turn on Open to Work (remote) | ☐ |

---

## Phase 2 — Project 1: Cloud API (Weeks 2–3)

**Folder:** `projects/cloud-api`

Shows: Node/Express, health checks, env config, Docker, CI.

| Week | Tasks |
|------|--------|
| 2 | Finish API routes (`/health`, `/api/info`), add JWT auth stub, write tests if time permits |
| 3 | `docker build` / `docker compose up`, document EC2 deploy in `DEPLOY.md`, run GitHub Actions on push |
| 3 | Screenshot: Postman + `docker ps` + browser `/health` |

**CV line (after deploy):** *Deployed containerized Node.js REST API on AWS EC2 with Docker and GitHub Actions CI.*

---

## Phase 3 — Project 2: Document AI Assistant (Weeks 4–5)

**Folder:** `projects/document-ai-assistant`

Shows: Python, FastAPI, RAG, vector DB, Docker — your **AI application engineer** story.

| Week | Tasks |
|------|--------|
| 4 | Upload PDFs, chunk, embed, ask questions via `/chat` |
| 4 | Simple React or static HTML frontend (optional) |
| 5 | Dockerize; same EC2 with reverse proxy (Nginx) or second port |
| 5 | README: architecture diagram (upload → chunks → Chroma → LLM) |

**CV line:** *Built RAG document Q&A service with FastAPI, ChromaDB, and LLM APIs; containerized for cloud deployment.*

---

## Phase 4 — Project 3: Full-stack mini MIS demo (Weeks 6–8) — optional but strong for PHP roles

**Suggested name:** `projects/mini-admission-demo`

- PHP 8 + MySQL **or** Laravel (learn Laravel here if you have time).
- Features: register, login, role-based admin, fake “payment status” (no real Razorpay keys in repo).
- Docker: PHP-FPM + Nginx + MySQL.

**CV line:** *Demo admission workflow with RBAC and payment-status API (pattern from production MIS work).*

---

## Phase 5 — AWS certificate (parallel)

- Month 1–2: AWS Cloud Practitioner (Skill Builder free tier).
- Mention on LinkedIn when passed; add under Certifications on CV.

---

## Interview stories (tie to portfolio)

| Topic | Your proof |
|-------|------------|
| Scale | NIELIT MIS 7k+ students; exam ops 15k+ candidates |
| Payments | Describe webhook + HMAC pattern; point to payment demo when built |
| RBAC | Admin roles in MIS; same pattern in mini-admission demo |
| Cloud | EC2 + Docker README steps you actually ran |
| AI | RAG project: chunking, embeddings, prompt boundaries |

---

## Application rhythm (while building)

- **10–15 targeted applications/week** on LinkedIn, Naukri, Indeed, Wellfound, Remotive.
- Keywords: `remote PHP`, `Laravel developer India`, `Junior DevOps`, `AI application developer`.
- After Project 1 is live, add **Live demo:** URL to CV header.

---

## Screenshot checklist (per project)

1. Architecture or folder structure in README  
2. UI or API response (Swagger at `/docs` for Python)  
3. Terminal: Docker or `git push` with green CI  

Store images in `projects/<name>/docs/images/` and reference them in README.
