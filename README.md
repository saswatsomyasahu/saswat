# Saswat Somya Sahu — Developer Portfolio

**Software Developer | PHP, Node.js, React | Cloud & AI**

[![Portfolio site](https://img.shields.io/badge/Portfolio-live-00e5c8?style=for-the-badge&logo=githubpages&logoColor=black)](https://saswatsomyasahu.github.io/saswat/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/saswatsomyasahu)

Public demos and infrastructure code: enterprise-style **PHP/MySQL**, **Node.js**, **Docker/CI**, and **RAG/LLM** apps.  
Production work: **NIELIT Bhubaneswar** (Ministry of Electronics and Information Technology — MeitY, Government of India).

## Live links

| Link | URL |
|------|-----|
| **Portfolio website** | https://saswatsomyasahu.github.io/saswat/ |
| **All projects (detail pages)** | https://saswatsomyasahu.github.io/saswat/projects/ |
| **Cloud API** | [`projects/cloud-api`](./projects/cloud-api/) |
| **Document AI (RAG)** | [`projects/document-ai-assistant`](./projects/document-ai-assistant/) |

> **GitHub Pages:** enable under **Settings → Pages → Source: GitHub Actions** (workflow included). See [docs/GITHUB_PAGES.md](./docs/GITHUB_PAGES.md).

## Repository layout

| Path | Description |
|------|-------------|
| [`docs/`](./docs/) | Bootstrap portfolio site (GitHub Pages) |
| [`docs/projects/`](./docs/projects/) | Per-project detail pages (MIS, payments, Jitsi, OMR, IoT, cloud, AI) |
| [`projects/cloud-api`](./projects/cloud-api/) | Node + Docker + Actions CI |
| [`projects/document-ai-assistant`](./projects/document-ai-assistant/) | FastAPI RAG + web UI |
| [`profile-readme/`](./profile-readme/) | Copy to `github.com/saswatsomyasahu/saswatsomyasahu` for profile README |
| [`PORTFOLIO_PLAN.md`](./PORTFOLIO_PLAN.md) | Build roadmap |

## Quick start (local)

```bash
# Portfolio site
cd docs && python -m http.server 8080

# Cloud API
cd projects/cloud-api && npm install && npm run dev

# Document AI
cd projects/document-ai-assistant
python -m venv .venv && .venv\Scripts\activate
pip install -r requirements.txt && cp .env.example .env
uvicorn app.main:app --reload
```

## Suggested GitHub repo topics

`portfolio` `php` `nodejs` `docker` `fastapi` `rag` `devops` `remote-developer` `fullstack-developer` `mongodb` `django` `laravel`

## Contact

- **Email:** saswatsomya111@gmail.com  
- **LinkedIn:** [linkedin.com/in/saswatsomyasahu](https://linkedin.com/in/saswatsomyasahu)  
- **Location:** Bhubaneswar, Odisha — **open to remote**

---

*Full Stack PHP/Node · Junior DevOps · Cloud & AI application roles.*
