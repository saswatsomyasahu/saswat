# Deploy `cloud-api` (AWS EC2 outline)

## Prerequisites

- AWS account, one EC2 instance (Ubuntu 22.04, `t3.micro` is enough for demo)
- Security group: inbound TCP **22** (your IP), **3000** or **80** (if using Nginx)

## On the server

```bash
sudo apt update && sudo apt install -y docker.io docker-compose-plugin git
sudo usermod -aG docker $USER
# log out and back in

git clone https://github.com/saswatsomyasahu/saswat.git
cd saswat/projects/cloud-api
docker compose up -d --build
curl http://127.0.0.1:3000/health
```

## Production tips

- Put **Nginx** in front with TLS (Let's Encrypt).
- Use **GitHub Actions** (see `.github/workflows/cloud-api-ci.yml`) to build/test on each push.
- Set `NODE_ENV=production` and restrict security group to 443 only.

## Railway / Render (faster than EC2)

- Connect repo, set root directory to `projects/cloud-api`, start command `npm start`.
- Add env vars from `.env.example`.
