# Saswat Somya Sahu — Developer Portfolio

**Software Developer | PHP, Node.js, React | Cloud & AI**

Public demos and infrastructure code that showcase enterprise web development, cloud deployment, and AI application engineering. Institutional work at NIELIT is not published here; these projects are **original implementations** of similar patterns (auth, APIs, payments concepts, document Q&A).

| Focus | What recruiters see |
|--------|---------------------|
| Full stack | REST APIs, React UI, MySQL/SQLite |
| Cloud / DevOps | Docker, AWS-ready deploy notes, GitHub Actions CI |
| AI apps | RAG chatbot over your own documents (LLM API) |

## Projects

| # | Project | Stack | Status |
|---|---------|-------|--------|
| 1 | [Cloud API + Docker](./projects/cloud-api/) | Node.js, Express, Docker, GitHub Actions | Starter — deploy to EC2 |
| 2 | [Document AI Assistant (RAG)](./projects/document-ai-assistant/) | Python, FastAPI, ChromaDB, Docker | Starter — add API key & run |
| 3 | [Portfolio website](./docs/) | Static HTML (GitHub Pages) | Enable Pages → `/docs` |

## Quick start (local)

```bash
# Cloud API
cd projects/cloud-api
cp .env.example .env
npm install && npm run dev

# Document AI (needs OPENAI_API_KEY or compatible endpoint in .env)
cd projects/document-ai-assistant
python -m venv .venv
.venv\Scripts\activate   # Windows
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

## Deploy on GitHub

1. Repo: **[github.com/saswatsomyasahu/saswat](https://github.com/saswatsomyasahu/saswat)**
2. From this folder (first time):

```bash
git init
git add README.md PORTFOLIO_PLAN.md .gitignore .github projects
git commit -m "Add portfolio hub and starter cloud/AI projects"
git branch -M main
git remote add origin https://github.com/saswatsomyasahu/saswat.git
git push -u origin main
```

3. Pin this repo on your GitHub profile and add the link to your CV and LinkedIn.

5. **Live site:** turn on GitHub Pages from the `/docs` folder — steps in [docs/GITHUB_PAGES.md](./docs/GITHUB_PAGES.md) → **https://saswatsomyasahu.github.io/saswat/**

6. **Profile README:** copy [profile-readme/README.md](./profile-readme/README.md) into a new repo named `saswatsomyasahu` — see [profile-readme/SETUP.md](./profile-readme/SETUP.md).

4. **Optional API demos:** deploy `cloud-api` to AWS EC2 or Railway; deploy `document-ai-assistant` behind Docker on the same host (see each project's `DEPLOY.md`).

## Roadmap

See [PORTFOLIO_PLAN.md](./PORTFOLIO_PLAN.md) for a week-by-week build order, screenshots checklist, and what to add to your CV after each milestone.

## Contact

- Email: saswatsomya111@gmail.com
- LinkedIn: [linkedin.com/in/saswatsomyasahu](https://linkedin.com/in/saswatsomyasahu)
- Location: Bhubaneswar, Odisha — open to **remote** roles

---

*Built for Cloud Support, Junior DevOps, Full Stack PHP/Node, and AI Application Developer roles — target compensation ₹40–45k/month (open to discussion).*
