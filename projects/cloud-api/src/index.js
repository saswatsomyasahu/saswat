import "dotenv/config";
import express from "express";
import cors from "cors";
import helmet from "helmet";

const app = express();
const port = Number(process.env.PORT) || 3000;

app.use(helmet());
app.use(cors());
app.use(express.json());

const startedAt = new Date().toISOString();

app.get("/health", (_req, res) => {
  res.json({
    status: "ok",
    service: process.env.APP_NAME || "cloud-api",
    uptimeSeconds: Math.floor(process.uptime()),
    timestamp: new Date().toISOString(),
  });
});

app.get("/api/info", (_req, res) => {
  res.json({
    author: "Saswat Somya Sahu",
    stack: ["Node.js", "Express", "Docker", "AWS EC2"],
    purpose: "Portfolio demo for cloud-ready REST APIs",
    startedAt,
  });
});

app.post("/api/echo", (req, res) => {
  res.json({ received: req.body ?? null });
});

app.use((_req, res) => {
  res.status(404).json({ error: "Not found" });
});

app.listen(port, () => {
  console.log(`cloud-api listening on http://localhost:${port}`);
});
