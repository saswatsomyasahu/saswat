# Cloud API (Node.js + Docker)

Minimal **production-style** REST API for your portfolio: health checks, JSON routes, Docker, and CI — the same patterns you use when deploying MIS and payment services.

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/health` | Liveness for load balancers / Docker |
| GET | `/api/info` | Metadata for portfolio README |
| POST | `/api/echo` | Echo JSON body (API test) |

## Run locally

```bash
cp .env.example .env
npm install
npm run dev
```

Open http://localhost:3000/health

## Docker

```bash
docker compose up --build
```

## Next steps (you implement)

1. Add JWT login stub (`/auth/login` returning a signed token).
2. Add GitHub Actions badge to this README after first green run.
3. Deploy using [DEPLOY.md](./DEPLOY.md) and paste **Live URL** in root portfolio README.

## Author

Saswat Somya Sahu — NIELIT enterprise web + server background; this repo is a clean public demo.
