const ROLES = [
  "cloud-ready APIs",
  "RAG / LLM apps",
  "PHP enterprise systems",
  "Docker pipelines",
  "full stack products",
];

const typeEl = document.getElementById("typewriter");
let roleIndex = 0;
let charIndex = 0;
let deleting = false;

function typeWriter() {
  if (!typeEl) return;
  const word = ROLES[roleIndex];
  if (!deleting) {
    typeEl.textContent = word.slice(0, charIndex + 1);
    charIndex += 1;
    if (charIndex === word.length) {
      deleting = true;
      setTimeout(typeWriter, 1800);
      return;
    }
  } else {
    typeEl.textContent = word.slice(0, charIndex - 1);
    charIndex -= 1;
    if (charIndex === 0) {
      deleting = false;
      roleIndex = (roleIndex + 1) % ROLES.length;
    }
  }
  setTimeout(typeWriter, deleting ? 45 : 85);
}

function initCounters() {
  const counters = document.querySelectorAll(".counter");
  const run = (el) => {
    const target = Number(el.dataset.target);
    const duration = 1600;
    const start = performance.now();
    const tick = (now) => {
      const p = Math.min((now - start) / duration, 1);
      const eased = 1 - (1 - p) ** 3;
      el.textContent = Math.floor(target * eased).toLocaleString("en-IN");
      if (p < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  };

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          run(entry.target);
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.3 }
  );

  counters.forEach((c) => observer.observe(c));
}

function initProgressBars() {
  const bars = document.querySelectorAll(".progress-glow .progress-bar");
  bars.forEach((bar) => {
    const w = bar.style.width;
    bar.style.width = "0";
    const obs = new IntersectionObserver(
      (entries) => {
        if (entries[0].isIntersecting) {
          bar.style.width = w;
          obs.disconnect();
        }
      },
      { threshold: 0.2 }
    );
    obs.observe(bar.parentElement);
  });
}

function initBackToTop() {
  const btn = document.getElementById("backToTop");
  if (!btn) return;
  window.addEventListener("scroll", () => {
    btn.classList.toggle("visible", window.scrollY > 400);
  });
  btn.addEventListener("click", () => window.scrollTo({ top: 0, behavior: "smooth" }));
}

document.getElementById("year").textContent = new Date().getFullYear();

AOS.init({
  duration: 700,
  easing: "ease-out-cubic",
  once: true,
  offset: 60,
});

document.querySelectorAll('[data-bs-toggle="tooltip"]').forEach((el) => {
  new bootstrap.Tooltip(el);
});

typeWriter();
initCounters();
initProgressBars();
initBackToTop();
