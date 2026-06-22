from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Daniyal Hussain · DevOps Portfolio</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { background: #0d1117; color: #e6edf3; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", monospace; min-height: 100vh; display: flex; align-items: center; justify-content: center; padding: 2rem; }
    .card { background: #161b22; border: 1px solid #30363d; border-radius: 12px; padding: 2rem; max-width: 720px; width: 100%; }
    .header { display: flex; align-items: center; gap: 16px; padding-bottom: 1.5rem; border-bottom: 1px solid #30363d; margin-bottom: 1.5rem; }
    .avatar { width: 48px; height: 48px; border-radius: 50%; background: #1d9e75; display: flex; align-items: center; justify-content: center; font-size: 16px; font-weight: 600; color: #e1f5ee; flex-shrink: 0; }
    .name { font-size: 20px; font-weight: 600; color: #e6edf3; }
    .role { font-size: 13px; color: #8b949e; margin-top: 2px; }
    .live-badge { margin-left: auto; background: rgba(29,158,117,0.15); color: #1d9e75; font-size: 11px; padding: 4px 12px; border-radius: 20px; border: 1px solid #1d9e75; white-space: nowrap; }
    .title { font-size: 22px; font-weight: 600; color: #58a6ff; margin-bottom: 4px; }
    .subtitle { font-size: 13px; color: #8b949e; margin-bottom: 1.5rem; }
    .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 10px; margin-bottom: 1.5rem; }
    .metric { background: #0d1117; border: 1px solid #30363d; border-radius: 8px; padding: 12px; }
    .metric-label { font-size: 11px; color: #8b949e; text-transform: uppercase; letter-spacing: 0.06em; margin-bottom: 4px; }
    .metric-value { font-size: 15px; font-weight: 500; color: #e6edf3; }
    .section-label { font-size: 11px; color: #8b949e; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 10px; }
    .stages { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 1.5rem; align-items: center; }
    .stage { background: rgba(29,158,117,0.12); color: #1d9e75; font-size: 12px; padding: 5px 12px; border-radius: 20px; border: 1px solid #1d9e75; }
    .arrow { color: #30363d; font-size: 14px; }
    .stack { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 1.5rem; }
    .tag { background: #0d1117; color: #58a6ff; font-size: 12px; padding: 4px 10px; border-radius: 6px; border: 1px solid #30363d; }
    .footer { border-top: 1px solid #30363d; padding-top: 1rem; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px; }
    .footer-text { font-size: 12px; color: #8b949e; }
    .footer-text span { color: #e6edf3; }
    .links { display: flex; gap: 16px; }
    .links a { font-size: 12px; color: #58a6ff; text-decoration: none; }
    .links a:hover { text-decoration: underline; }
  </style>
</head>
<body>
  <div class="card">
    <div class="header">
      <div class="avatar">DH</div>
      <div>
        <div class="name">Daniyal Hussain</div>
        <div class="role">DevOps Engineer &middot; Barani Institute of Sciences</div>
      </div>
      <div class="live-badge">&#9679; LIVE</div>
    </div>

    <div class="title">CI/CD Pipeline &mdash; AWS EC2</div>
    <div class="subtitle">Automatically deployed via GitHub Actions &rarr; Docker &rarr; Nginx &rarr; EC2</div>

    <div class="grid">
      <div class="metric"><div class="metric-label">Environment</div><div class="metric-value">Production</div></div>
      <div class="metric"><div class="metric-label">Container</div><div class="metric-value">Docker &middot; Alpine</div></div>
      <div class="metric"><div class="metric-label">Web Server</div><div class="metric-value">Nginx &middot; Port 80</div></div>
      <div class="metric"><div class="metric-label">Platform</div><div class="metric-value">AWS EC2</div></div>
    </div>

    <div class="section-label">Pipeline Stages</div>
    <div class="stages">
      <span class="stage">&#10003; Code</span>
      <span class="arrow">&rarr;</span>
      <span class="stage">&#10003; Build</span>
      <span class="arrow">&rarr;</span>
      <span class="stage">&#10003; Test</span>
      <span class="arrow">&rarr;</span>
      <span class="stage">&#10003; Push</span>
      <span class="arrow">&rarr;</span>
      <span class="stage">&#10003; Deploy</span>
    </div>

    <div class="section-label">Tech Stack</div>
    <div class="stack">
      <span class="tag">GitHub Actions</span>
      <span class="tag">Docker</span>
      <span class="tag">AWS EC2</span>
      <span class="tag">Nginx</span>
      <span class="tag">Ansible</span>
      <span class="tag">Flask &middot; Python</span>
    </div>

    <div class="footer">
      <div class="footer-text">Deployed by: <span>Daniyal Hussain</span> &middot; Batch 2026</div>
      <div class="links">
        <a href="https://github.com/Daniyal656" target="_blank">GitHub</a>
        <a href="https://linkedin.com/in/daniyal-hussain-2555b62a4" target="_blank">LinkedIn</a>
      </div>
    </div>
  </div>
</body>
</html>'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
