# Update your GitHub profile README

Your profile README lives in repo **`saswatsomyasahu/saswatsomyasahu`** (name = your username).

## If the repo does not exist yet

1. Open https://github.com/new  
2. Repository name: **`saswatsomyasahu`** (exactly your username)  
3. Public · check **Add a README** → Create  
4. Run the push commands below (replace README content)

## Push from your PC

```powershell
cd d:\Projects\portfolies\profile-readme
git init
git add README.md
git commit -m "Update GitHub profile README"
git branch -M main
git remote add origin https://github.com/saswatsomyasahu/saswatsomyasahu.git
git push -u origin main --force
```

> Use `--force` only if GitHub created a default README and you need to overwrite it once.

## Pin & polish on GitHub.com

1. Open https://github.com/saswatsomyasahu → confirm README shows at top  
2. **Pin** repo [saswat](https://github.com/saswatsomyasahu/saswat) on your profile  
3. Repo **saswat** → ⚙️ About → add description + website: `https://saswatsomyasahu.github.io/saswat/`  
4. Add topics: `portfolio` `php` `nodejs` `docker` `fastapi` `django` `mongodb` `devops`

## Enable portfolio site (if 404)

**saswat** → Settings → Pages → **Source: GitHub Actions** → run workflow *Deploy portfolio to GitHub Pages*.
