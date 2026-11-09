# GitHub Profile README setup

Your profile README must live in a repo named **exactly** like your username: `saswatsomyasahu/saswatsomyasahu`.

## One-time on GitHub

1. Go to [github.com/new](https://github.com/new)
2. Repository name: `saswatsomyasahu` (same as username)
3. Public · add a README · Create repository
4. Replace the default README with the contents of `profile-readme/README.md` in this folder (copy/paste or push below)

## Push from this PC (after repo exists)

```powershell
cd d:\Projects\portfolies\profile-readme
git init
git add README.md
git commit -m "Add GitHub profile README"
git branch -M main
git remote add origin https://github.com/saswatsomyasahu/saswatsomyasahu.git
git push -u origin main
```

Visit https://github.com/saswatsomyasahu — the README appears at the top of your profile.
