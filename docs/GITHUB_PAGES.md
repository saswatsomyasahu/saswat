# GitHub Pages — fix wrong site (README text) or 404

## If you see plain README / `**bold**` markdown (not the dark portfolio)

GitHub is publishing the **repo root**, not the `docs/` website.

**Fix A (recommended):** Settings → Pages → **Source: GitHub Actions** → run workflow *Deploy portfolio to GitHub Pages*.

**Fix B:** Settings → Pages → **Deploy from branch** → branch **main** → folder **`/docs`** (not `/` root).

After save, wait 2–3 minutes and hard-refresh `https://saswatsomyasahu.github.io/saswat/`.

A root `index.html` redirect to `docs/` is included as a temporary fallback if root deploy is selected by mistake.

---

# GitHub Pages — fix “site not found” (404)

If **https://saswatsomyasahu.github.io/saswat/** shows *Site not found*, Pages is not enabled yet.

## Option A — GitHub Actions (recommended)

This repo includes `.github/workflows/pages.yml`. After you push to `main`:

1. Open **Settings** → **Pages**  
   https://github.com/saswatsomyasahu/saswat/settings/pages  
2. Under **Build and deployment**, set **Source** to **GitHub Actions** (not “Deploy from branch”).  
3. Run the workflow: **Actions** tab → **Deploy portfolio to GitHub Pages** → **Run workflow** (or wait for the next push).  
4. In 1–3 minutes, the site should load at:
   - https://saswatsomyasahu.github.io/saswat/
   - https://saswatsomyasahu.github.io/saswat/demos/document-ai-assistant/

## Option B — Deploy from branch

1. **Settings** → **Pages**  
2. Source: **Deploy from a branch**  
3. Branch: **main**, folder: **/docs** → **Save**

## Document AI — what opens where

| URL | What it is |
|-----|------------|
| GitHub tree link | Source code only — not a running app |
| `…/demos/document-ai-assistant/` | Explains how to run (works on GitHub Pages) |
| `http://127.0.0.1:8000/` | **Live chat UI** — only when you run `uvicorn` on your PC |

The RAG API cannot run on free GitHub Pages (needs Python + your OpenAI key on a server).
