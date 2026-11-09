"""Update Saswat's CV docx with portfolio and cloud/AI alignment."""
from docx import Document
from pathlib import Path

CV_PATH = Path(r"d:\Projects\portfolies\Saswat_Somya_Sahu_CV.docx")

HEADLINE = "Software Developer | PHP, Node.js, React | Cloud & AI"

CONTACT = (
    "Bhubaneswar, Odisha 751013, India | saswatsomya111@gmail.com | +91 76538 14034 | "
    "linkedin.com/in/saswatsomyasahu | github.com/saswatsomyasahu/saswat | "
    "Portfolio: saswatsomyasahu.github.io/saswat"
)

SUMMARY = (
    "Software Developer with 2+ years at NIELIT Bhubaneswar, building enterprise web systems "
    "(PHP/MySQL, Node.js, React) and managing government IT infrastructure (Linux, AWS, Docker, CI/CD). "
    "Delivered student MIS (7,000+ registrations), Razorpay payment portal with webhooks, exam server "
    "operations (15,000+ candidates), and reporting integrations. Public portfolio on GitHub features "
    "containerized APIs and a RAG document assistant (FastAPI, ChromaDB, LLM APIs). "
    "Open to remote roles in Full Stack PHP/Node, Junior DevOps / Cloud Support, and AI Application Development."
)

SKILLS = {
    6: "Programming: PHP, JavaScript, Node.js, Python, Java, SQL",
    7: "Frontend: HTML, CSS, Bootstrap, React.js",
    8: (
        "Backend and APIs: PHP, Laravel, Node.js, Express.js, Python, Django, FastAPI, REST APIs, "
        "Webhooks, JWT, Role-Based Access Control"
    ),
    9: "Database: MySQL, MongoDB, Schema Design, Migrations, SQL",
    10: (
        "Libraries and Integrations: Razorpay, PHPMailer (SMTP), TCPDF, PhpSpreadsheet, "
        "Biometric (SecuGen) APIs, OpenAI/LLM APIs, ChromaDB (RAG)"
    ),
    11: (
        "Servers, Cloud and Networking: Linux, AWS (EC2), Apache, Nginx, cPanel, Docker, "
        "Server Deployment, Routers, Switches, Firewalls, Backup and Monitoring"
    ),
    12: "Tools: Git, GitHub, GitHub Actions, Docker, CI/CD, XAMPP, Composer",
    13: "Domain: Education MIS, Government Schemes, Training Partner Reporting; Cloud & AI demos",
}

PORTFOLIO_BLOCKS = [
    (
        "Portfolio — Cloud API | Node.js, Express, Docker, GitHub Actions (GitHub: saswatsomyasahu/saswat)",
        "REST API with health checks and JSON routes; Dockerfile, Docker Compose, and CI workflow "
        "for cloud deployment (AWS EC2 / Railway). Demonstrates production-style ops alongside NIELIT deployments.",
    ),
    (
        "Portfolio — Document AI Assistant (RAG) | Python, FastAPI, ChromaDB, LLM APIs",
        "Upload PDFs, chunk and embed content, answer questions via retrieval-augmented generation. "
        "Swagger-documented API, Dockerized stack; extends ML/OMR and IoT project experience into modern AI apps.",
    ),
]


def main() -> None:
    doc = Document(CV_PATH)
    paras = doc.paragraphs

    paras[1].text = HEADLINE
    paras[2].text = CONTACT
    paras[4].text = SUMMARY

    for idx, text in SKILLS.items():
        paras[idx].text = text

    # Insert portfolio projects after "KEY PROJECTS" heading (paragraph index 31)
    insert_at = 32
    for title, body in reversed(PORTFOLIO_BLOCKS):
        paras[insert_at].insert_paragraph_before(body)
        paras[insert_at].insert_paragraph_before(title)

    doc.save(CV_PATH)
    print(f"Updated {CV_PATH}")


if __name__ == "__main__":
    main()
