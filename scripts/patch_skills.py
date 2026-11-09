from pathlib import Path

p = Path(r"d:\Projects\portfolies\docs\index.html")
text = p.read_text(encoding="utf-8")
start = text.find('        <div class="row g-3" data-aos="fade-up" data-aos-delay="100">')
end = text.find('        <div class="progress-stack mt-4"', start)
new_block = '''        <div class="row g-3" data-aos="fade-up" data-aos-delay="100">
          <div class="col-lg-4">
            <h3 class="h6 text-secondary mb-3">Full stack · PHP / Node</h3>
            <div class="skills-cloud">
              <span class="skill-pill" data-bs-toggle="tooltip" title="Production MIS">PHP</span>
              <span class="skill-pill">Laravel</span>
              <span class="skill-pill">JavaScript</span>
              <span class="skill-pill">Node.js</span>
              <span class="skill-pill">Express.js</span>
              <span class="skill-pill">React</span>
              <span class="skill-pill">Bootstrap</span>
              <span class="skill-pill">REST APIs</span>
              <span class="skill-pill">JWT / RBAC</span>
            </div>
          </div>
          <div class="col-lg-4">
            <h3 class="h6 text-secondary mb-3">Python · Databases</h3>
            <div class="skills-cloud">
              <span class="skill-pill highlight-ai">Python</span>
              <span class="skill-pill highlight-ai">Django</span>
              <span class="skill-pill highlight-ai">FastAPI</span>
              <span class="skill-pill">MySQL</span>
              <span class="skill-pill" data-bs-toggle="tooltip" title="NoSQL document database">MongoDB</span>
              <span class="skill-pill">SQL</span>
              <span class="skill-pill highlight-ai">RAG / LLM</span>
            </motion>
          </motion>
          <motion class="col-lg-4">
            <h3 class="h6 text-secondary mb-3">Cloud · DevOps</h3>
            <div class="skills-cloud">
              <span class="skill-pill highlight">AWS EC2</span>
              <span class="skill-pill highlight">Docker</span>
              <span class="skill-pill highlight">GitHub Actions</span>
              <span class="skill-pill highlight">Linux</span>
              <span class="skill-pill highlight">Nginx</span>
              <span class="skill-pill highlight">CI/CD</span>
              <span class="skill-pill">Git</span>
            </div>
          </motion>
        </motion>
'''
new_block = new_block.replace("<motion ", "<div ").replace("</motion>", "</div>")
if start == -1 or end == -1:
    raise SystemExit("markers not found")
p.write_text(text[:start] + new_block + text[end:], encoding="utf-8")
print("patched skills section")
