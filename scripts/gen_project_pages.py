"""Generate static project detail pages."""
from pathlib import Path

OUT = Path(r"d:\Projects\portfolies\docs\projects")

NIELIT_ORG = (
    "National Institute of Electronics and Information Technology (NIELIT), Bhubaneswar — "
    "Ministry of Electronics and Information Technology (MeitY), Government of India"
)

PROJECTS = [
    {
        "file": "nielit-mis.html",
        "title": "NIELIT Bhubaneswar Student Management System (MIS)",
        "label": "Enterprise",
        "label_class": "php",
        "icon": "bi-mortarboard",
        "stack": ["PHP", "MySQL", "JavaScript", "Bootstrap", "RBAC", "PHPMailer", "TCPDF"],
        "org": NIELIT_ORG,
        "meity": True,
        "availability": "Production (institutional — source not public)",
        "overview": (
            "End-to-end web MIS for student registration, admissions, batches, government scheme tracking "
            "and administration across multiple centres — with 7,000+ registered candidates."
        ),
        "bullets": [
            "Online registration, document upload, OTP verification, student dashboards, courses, batches and certificates.",
            "Role-based admin access (Master Admin, Course Coordinator, Data Entry, Report Viewer).",
            "Multi-centre support, QR-based course registration, PDF application forms.",
            "Bulk student onboarding via Excel upload with automatic Student ID generation.",
            "Batch management: auto batch codes, seat limits, enrollment tracking, admission order generation (Word/PDF).",
            "Training partner & scheme reporting with Excel import/export and Certified/Placed tracking.",
            "Biometric fingerprint integration for verification and attendance.",
            "Automated email notifications, PDF/Excel generation and administrative dashboards.",
        ],
    },
    {
        "file": "payment-portal.html",
        "title": "Central Payment Portal",
        "label": "Payments",
        "label_class": "php",
        "icon": "bi-credit-card",
        "stack": ["PHP", "MySQL", "Razorpay API", "HMAC", "Webhooks", "REST"],
        "org": NIELIT_ORG,
        "meity": True,
        "availability": "Production (institutional — source not public)",
        "overview": (
            "Standalone payment application with its own database and admin console, integrated with the main MIS "
            "via secure signed requests."
        ),
        "bullets": [
            "Razorpay Checkout, payment capture, refunds and credit notes.",
            "Webhook handling for asynchronous payment status updates.",
            "Signed APIs for payment status, receipts and invoices.",
            "Secure hub-to-MIS integration — production secrets kept outside version control.",
            "Admin console for finance and course coordinators.",
        ],
    },
    {
        "file": "jitsi-online-classes.html",
        "title": "Online Classes Infrastructure (Jitsi Meet)",
        "label": "Infrastructure",
        "label_class": "cloud",
        "icon": "bi-camera-video",
        "stack": ["Linux", "Nginx", "Jitsi", "JWT", "Shell", "Python"],
        "org": NIELIT_ORG,
        "meity": True,
        "availability": "Production planning & integration",
        "overview": (
            "Self-hosted video conferencing for large online classes with JWT authentication, "
            "load testing and portal integration."
        ),
        "bullets": [
            "Planned and scripted self-hosted Jitsi deployment on Linux with Nginx reverse proxy.",
            "JWT authentication to gate room access from the student portal.",
            "Load testing for concurrent class sizes.",
            "Integrated into the student portal online classes module.",
        ],
    },
    {
        "file": "omr-android.html",
        "title": "NIST Teaching Assistant — OMR Sheet Checking",
        "label": "ML / Mobile",
        "label_class": "ai",
        "icon": "bi-phone",
        "stack": ["Java", "Android", "Python", "Image Processing", "Machine Learning"],
        "org": "National Institute of Science & Technology (academic project)",
        "availability": "Academic project",
        "overview": "Android app that automates OMR sheet evaluation using image recognition and machine learning models.",
        "bullets": [
            "Camera / image capture of OMR sheets.",
            "Image preprocessing and bubble detection.",
            "Scoring and result export for educators.",
            "Bridges mobile UX with Python-side ML workflows.",
        ],
    },
    {
        "file": "iot-weather.html",
        "title": "NIST Weather Station (IoT)",
        "label": "IoT",
        "label_class": "cloud",
        "icon": "bi-cloud-sun",
        "stack": ["IoT sensors", "React.js", "Node.js", "Express.js", "REST"],
        "org": "National Institute of Science & Technology (academic project)",
        "availability": "Academic project",
        "overview": "Real-time weather data from sensors displayed on a responsive web dashboard backed by Node.js.",
        "bullets": [
            "Sensor data acquisition and serial / gateway ingestion.",
            "Node.js + Express API for live readings.",
            "React dashboard with responsive UI.",
            "Foundation for monitoring-style full-stack work.",
        ],
    },
    {
        "file": "cloud-api.html",
        "title": "Cloud API (Portfolio)",
        "label": "Open source",
        "label_class": "cloud",
        "icon": "bi-cloud-arrow-up",
        "stack": ["Node.js", "Express", "Docker", "GitHub Actions"],
        "org": "Personal portfolio",
        "availability": "Public on GitHub",
        "overview": "Container-ready REST API demonstrating health checks, Docker, Compose and CI for cloud deploy roles.",
        "bullets": [
            "GET /health for load balancers and Docker HEALTHCHECK.",
            "/api/info and /api/echo for integration testing.",
            "Dockerfile + docker-compose.yml.",
            "GitHub Actions workflow on push.",
            "Deploy notes for AWS EC2 and Railway.",
        ],
        "link": "https://github.com/saswatsomyasahu/saswat/tree/main/projects/cloud-api",
    },
    {
        "file": "document-ai-assistant.html",
        "title": "Document AI Assistant (RAG)",
        "label": "Open source",
        "label_class": "ai",
        "icon": "bi-robot",
        "stack": ["Python", "FastAPI", "ChromaDB", "OpenAI API", "Docker"],
        "org": "Personal portfolio",
        "availability": "Public on GitHub — run locally",
        "overview": "Upload PDFs, embed chunks in ChromaDB, answer questions with retrieval-augmented generation (LLM).",
        "bullets": [
            "POST /documents/upload for PDF ingestion and chunk indexing.",
            "POST /chat for RAG Q&A with source filenames.",
            "Swagger at /docs and Bootstrap web UI at /.",
            "Docker Compose for repeatable demos.",
            "Demonstrates AI application engineering (not model training).",
        ],
        "link": "https://github.com/saswatsomyasahu/saswat/tree/main/projects/document-ai-assistant",
        "extra_link": "../demos/document-ai-assistant/",
        "extra_label": "How to run demo",
    },
]


def render(p: dict) -> str:
    chips = "".join(f"<span>{s}</span>" for s in p["stack"][:6])
    list_items = "\n".join(f"            <li>{b}</li>" for b in p["bullets"])
    stack_pills = "\n".join(f'            <span class="skill-pill">{s}</span>' for s in p["stack"])
    links = ""
    if p.get("link"):
        links += (
            f'<a href="{p["link"]}" class="btn btn-accent w-100 mt-3" target="_blank" rel="noopener">'
            f'<i class="bi bi-github me-1"></i> View on GitHub</a>'
        )
    if p.get("extra_link"):
        links += (
            f'<a href="{p["extra_link"]}" class="btn btn-outline-light w-100 mt-2">'
            f'{p.get("extra_label", "Demo")}</a>'
        )
    overview_short = (p["overview"][:155] + "…") if len(p["overview"]) > 155 else p["overview"]
    meity_badge = ""
    if p.get("meity"):
        meity_badge = (
            '<p class="mb-2">'
            '<span class="badge text-bg-dark border font-mono" style="border-color: rgba(0,229,200,.35)!important;color:#00e5c8;">'
            '<i class="bi bi-shield-check me-1"></i> MeitY · Government of India'
            "</span></p>"
        )

    return f"""<!DOCTYPE html>
<html lang="en" data-bs-theme="dark">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{p["title"]} | Saswat Somya Sahu</title>
  <meta name="description" content="{overview_short}" />
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" />
  <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css" rel="stylesheet" />
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../styles.css" />
  <link rel="stylesheet" href="project.css" />
</head>
<body>
  <div class="bg-grid" aria-hidden="true"></div>
  <nav class="navbar navbar-dark project-nav fixed-top">
    <div class="container">
      <a class="navbar-brand font-mono" href="../index.html#projects"><i class="bi bi-arrow-left me-2"></i>Portfolio</a>
      <a class="btn btn-sm btn-outline-light" href="index.html">All projects</a>
    </div>
  </nav>

  <main class="container project-page" style="padding-top: 5.5rem;">
    <header class="project-hero">
      <span class="project-label {p["label_class"]}"><i class="bi {p["icon"]}"></i> {p["label"]}</span>
      <h1 class="mt-3">{p["title"]}</h1>
      {meity_badge}
      <p class="text-body-secondary mb-3">{p["overview"]}</p>
      <div class="chip-row font-mono">{chips}</div>
    </header>

    <div class="row g-4">
      <div class="col-lg-8">
        <div class="glass-card">
          <h2 class="h5 text-light">Key features &amp; responsibilities</h2>
          <ul class="feature-list mt-3 mb-0">
{list_items}
          </ul>
        </div>
      </div>
      <div class="col-lg-4">
        <div class="glass-card mb-4">
          <h2 class="h6 text-secondary">Organization</h2>
          <p class="mb-2">{p["org"]}</p>
          <h2 class="h6 text-secondary mt-3">Availability</h2>
          <p class="small text-body-secondary mb-0">{p["availability"]}</p>
        </div>
        <div class="glass-card">
          <h2 class="h6 text-secondary">Tech stack</h2>
          <div class="skills-cloud mt-2">
{stack_pills}
          </div>
          {links}
        </div>
      </div>
    </div>
  </main>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
""".replace("</motion>", "</div>").replace("<motion ", "<div ").replace("</direction>", "</div>")


def main() -> None:
    for p in PROJECTS:
        (OUT / p["file"]).write_text(render(p), encoding="utf-8")
        print("wrote", p["file"])


if __name__ == "__main__":
    main()
