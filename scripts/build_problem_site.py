#!/usr/bin/env python3
import html
import re
from pathlib import Path
from typing import Dict, List, Tuple

ROOT = Path(__file__).resolve().parent.parent
QUESTION_DIR = ROOT / "question"
CODE_DIRS = [ROOT / "src", ROOT / "test"]
OUTPUT_DIR = ROOT / "docs"

CSS = """
:root {
  --bg: #f4efe4;
  --ink: #211c15;
  --paper: #fffaf0;
  --paper-2: #fff4df;
  --accent: #b43b1d;
  --line: #d8c2a3;
  --line-strong: #b7966c;
  --muted: #615545;
  --shadow: 0 20px 40px rgba(43, 31, 17, 0.12);
}
[data-theme="dark"] {
  --bg: #181512;
  --ink: #efe4d2;
  --paper: #26211c;
  --paper-2: #2d2721;
  --accent: #ff8d5e;
  --line: #4b4134;
  --line-strong: #78644d;
  --muted: #c4b39c;
  --shadow: 0 20px 36px rgba(0, 0, 0, 0.35);
}
* { box-sizing: border-box; }
body {
  margin: 0;
  color: var(--ink);
  background:
    radial-gradient(circle at 8% -10%, #ffe6be 0%, transparent 38%),
    radial-gradient(circle at 92% 110%, #ffd8b0 0%, transparent 34%),
    linear-gradient(120deg, transparent 0 46%, rgba(255,255,255,0.35) 46% 47%, transparent 47%),
    var(--bg);
  font-family: "Noto Serif SC", "Source Han Serif SC", serif;
}
body::before {
  content: "";
  position: fixed;
  inset: 0;
  pointer-events: none;
  background-image: radial-gradient(rgba(107, 84, 48, 0.08) 0.8px, transparent 0.8px);
  background-size: 4px 4px;
  opacity: .4;
  z-index: -1;
}
a { color: inherit; }
.home-wrap {
  max-width: 1140px;
  margin: 0 auto;
  padding: 40px 22px 68px;
}
.theme-toggle {
  position: fixed;
  right: 16px;
  top: 14px;
  z-index: 20;
  border: 1px solid var(--line-strong);
  background: var(--paper);
  color: var(--ink);
  border-radius: 999px;
  padding: 6px 12px;
  font: inherit;
  font-size: .82rem;
  cursor: pointer;
}
.hero {
  border: 1px solid var(--line-strong);
  background: linear-gradient(145deg, var(--paper), #fff7e8);
  border-radius: 20px;
  padding: 28px 24px;
  box-shadow: var(--shadow);
  position: relative;
  overflow: hidden;
}
.hero::after {
  content: "";
  position: absolute;
  right: -20px;
  top: -20px;
  width: 160px;
  height: 160px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(180, 59, 29, .26) 0%, transparent 68%);
}
.home-title {
  margin: 10px 0 0;
  font-size: clamp(2.1rem, 4vw, 3.4rem);
  letter-spacing: 0.6px;
  line-height: 1.1;
  max-width: 16ch;
  font-weight: 700;
}
.eyebrow {
  display: inline-block;
  padding: 4px 10px;
  border-radius: 999px;
  border: 1px solid var(--line-strong);
  background: #fffdf8;
  color: var(--accent);
  font-size: 0.82rem;
  letter-spacing: .08em;
}
.home-sub {
  margin-top: 12px;
  color: var(--muted);
  max-width: 70ch;
  line-height: 1.75;
}
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(270px, 1fr));
  gap: 18px;
  margin-top: 22px;
}
.card {
  display: block;
  text-decoration: none;
  background: linear-gradient(160deg, var(--paper) 0%, #fffdf8 100%);
  border: 1px solid var(--line);
  border-radius: 18px;
  padding: 18px;
  min-height: 150px;
  box-shadow: 0 8px 24px rgba(57, 39, 20, 0.08);
  transition: transform .2s ease, box-shadow .2s ease, border-color .2s ease;
  animation: rise .45s ease both;
}
.card:hover {
  transform: translateY(-4px);
  border-color: var(--accent);
  box-shadow: 0 16px 30px rgba(61, 34, 10, .16);
}
.card-id {
  color: #8f2b12;
  font-size: .85rem;
  font-weight: 600;
  letter-spacing: .06em;
}
.card-title {
  margin-top: 8px;
  font-size: 1.25rem;
  line-height: 1.3;
}
.card-meta {
  margin-top: 12px;
  color: var(--muted);
  font-size: .9rem;
}
.layout {
  display: flex;
  gap: 0;
  min-height: 100vh;
  max-width: 1500px;
  margin: 0 auto;
  border-left: 1px solid var(--line);
  border-right: 1px solid var(--line);
}
.panel {
  padding: 28px 24px 42px;
  overflow: auto;
  animation: fadein .45s ease both;
}
.left {
  flex: 0 0 46%;
  background: linear-gradient(180deg, #fff8eb 0%, #fffef9 100%);
  border-right: 1px solid var(--line-strong);
}
.right {
  flex: 1;
  background: linear-gradient(180deg, #fdf3de 0%, #f9edd6 100%);
}
.topbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 18px;
}
.badge {
  display: inline-block;
  padding: 5px 12px;
  border-radius: 999px;
  border: 1px solid var(--line-strong);
  font-size: .82rem;
  color: #7f3019;
  background: #fff;
}
.back {
  text-decoration: none;
  border: 1px solid var(--line-strong);
  padding: 8px 12px;
  border-radius: 10px;
  background: #fffdfa;
  font-size: .9rem;
  transition: background .2s ease;
}
.back:hover { background: #fff3de; }
h1,h2,h3,h4 {
  margin-top: 1.1em;
  margin-bottom: .5em;
  line-height: 1.3;
}
h1 { font-size: clamp(1.8rem, 2.3vw, 2.4rem); }
h2 { font-size: 1.35rem; }
p { line-height: 1.8; margin: .65em 0; }
ul, ol { line-height: 1.8; padding-left: 22px; }
li { margin: .3em 0; }
pre {
  border-radius: 14px;
  border: 1px solid #293646;
  margin: 8px 0 18px;
  overflow: hidden;
  box-shadow: 0 10px 22px rgba(35, 36, 50, 0.18);
}
pre code {
  display: block;
  border-radius: inherit;
  font-family: "Fira Code", "JetBrains Mono", monospace;
  font-size: .88rem;
}
.code-block h3 {
  margin: 0;
  font-size: .92rem;
  color: #3f3327;
}
.code-head {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 10px;
  gap: 12px;
}
.path {
  color: var(--muted);
  font-size: .8rem;
  word-break: break-all;
}
.code-intro {
  margin: 8px 0 14px;
  color: #5f4e39;
  font-size: .95rem;
}
[data-theme="dark"] body {
  background:
    radial-gradient(circle at 8% -10%, rgba(255, 141, 94, 0.22) 0%, transparent 38%),
    radial-gradient(circle at 92% 110%, rgba(255, 193, 140, 0.12) 0%, transparent 34%),
    linear-gradient(120deg, transparent 0 46%, rgba(255,255,255,0.03) 46% 47%, transparent 47%),
    var(--bg);
}
[data-theme="dark"] body::before {
  background-image: radial-gradient(rgba(255, 240, 220, 0.05) 0.8px, transparent 0.8px);
}
[data-theme="dark"] .hero {
  background: linear-gradient(145deg, #2b241d, #241f1a);
}
[data-theme="dark"] .eyebrow {
  background: #302922;
}
[data-theme="dark"] .card {
  background: linear-gradient(160deg, #2c2620 0%, #26211d 100%);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
}
[data-theme="dark"] .card-id,
[data-theme="dark"] .badge {
  color: #ffb089;
}
[data-theme="dark"] .layout {
  border-left-color: var(--line);
  border-right-color: var(--line);
}
[data-theme="dark"] .left {
  background: linear-gradient(180deg, #25201b 0%, #211c18 100%);
}
[data-theme="dark"] .right {
  background: linear-gradient(180deg, #1f1b17 0%, #1a1714 100%);
}
[data-theme="dark"] .badge,
[data-theme="dark"] .back {
  background: #302922;
}
[data-theme="dark"] .back:hover {
  background: #3a3128;
}
[data-theme="dark"] .code-block h3,
[data-theme="dark"] .code-intro,
[data-theme="dark"] .path {
  color: #d7c9b4;
}
.card:nth-child(2n) { animation-delay: .06s; }
.card:nth-child(3n) { animation-delay: .1s; }
@keyframes rise {
  from { opacity: 0; transform: translateY(8px); }
  to { opacity: 1; transform: translateY(0); }
}
@keyframes fadein {
  from { opacity: .3; }
  to { opacity: 1; }
}
@media (max-width: 900px) {
  .layout {
    display: block;
    border-left: 0;
    border-right: 0;
  }
  .left { border-right: 0; border-bottom: 1px solid var(--line-strong); }
  .home-wrap { padding-top: 28px; }
  .hero { padding: 22px 18px; }
  .panel { padding: 22px 16px 28px; }
}
"""


def extract_index(stem: str) -> str:
  match = re.match(r"^(\d+)", stem)
  if match:
    return match.group(1)
  return stem


def nice_title(path: Path) -> str:
  stem = path.stem
  parts = stem.split("_", 1)
  if len(parts) == 2:
    return parts[1]
  return stem


def markdown_to_html(text: str) -> str:
  lines = text.splitlines()
  out: List[str] = []
  in_code = False
  code_lang = ""
  in_ul = False

  def close_list() -> None:
    nonlocal in_ul
    if in_ul:
      out.append("</ul>")
      in_ul = False

  for raw in lines:
    line = raw.rstrip("\n")
    code_open = re.match(r"^```([\w+-]*)\s*$", line)
    if code_open:
      if in_code:
        out.append("</code></pre>")
        in_code = False
        code_lang = ""
      else:
        close_list()
        code_lang = code_open.group(1).strip()
        cls = f' class="language-{code_lang}"' if code_lang else ""
        out.append(f"<pre><code{cls}>")
        in_code = True
      continue

    if in_code:
      out.append(html.escape(raw))
      continue

    if not line.strip():
      close_list()
      continue

    heading = re.match(r"^(#{1,4})\s+(.*)$", line)
    if heading:
      close_list()
      level = len(heading.group(1))
      out.append(f"<h{level}>{html.escape(heading.group(2))}</h{level}>")
      continue

    bullet = re.match(r"^[-*]\s+(.*)$", line)
    if bullet:
      if not in_ul:
        out.append("<ul>")
        in_ul = True
      out.append(f"<li>{html.escape(bullet.group(1))}</li>")
      continue

    close_list()
    out.append(f"<p>{html.escape(line)}</p>")

  close_list()
  if in_code:
    out.append("</code></pre>")

  return "\n".join(out)


def page_shell(title: str, body: str, extra_head: str = "") -> str:
  return f"""<!doctype html>
<html lang=\"zh-CN\">
<head>
  <meta charset=\"UTF-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />
  <title>{html.escape(title)}</title>
  <link rel=\"preconnect\" href=\"https://fonts.googleapis.com\" />
  <link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin />
  <link href=\"https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;600;700&family=Fira+Code:wght@400;500&display=swap\" rel=\"stylesheet\" />
  <link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/atom-one-dark.min.css\" />
  <style>{CSS}</style>
  {extra_head}
</head>
<body>
<button id=\"theme-toggle\" class=\"theme-toggle\" type=\"button\" aria-label=\"切换深色主题\">深色</button>
{body}
<script src=\"https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js\"></script>
<script>
(() => {{
  const key = "problem_site_theme";
  const root = document.documentElement;
  const btn = document.getElementById("theme-toggle");
  const preferredDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
  const saved = localStorage.getItem(key);
  const apply = (theme) => {{
    root.setAttribute("data-theme", theme);
    if (btn) btn.textContent = theme === "dark" ? "浅色" : "深色";
  }};
  apply(saved || (preferredDark ? "dark" : "light"));
  if (btn) {{
    btn.addEventListener("click", () => {{
      const next = root.getAttribute("data-theme") == "dark" ? "light" : "dark";
      localStorage.setItem(key, next);
      apply(next);
    }});
  }}
  hljs.highlightAll();
}})();
</script>
</body>
</html>
"""


def collect_files() -> Tuple[Dict[str, Path], Dict[str, List[Path]]]:
  questions: Dict[str, Path] = {}
  for md in sorted(QUESTION_DIR.glob("*.md")):
    questions[extract_index(md.stem)] = md

  code_map: Dict[str, List[Path]] = {}
  for d in CODE_DIRS:
    if not d.exists():
      continue
    for path in sorted(d.glob("*")):
      if path.is_file():
        idx = extract_index(path.stem)
        code_map.setdefault(idx, []).append(path)

  return questions, code_map


def build_problem_page(idx: str, q_path: Path, code_paths: List[Path]) -> str:
  q_title = nice_title(q_path)
  q_html = markdown_to_html(q_path.read_text(encoding="utf-8"))

  code_parts = []
  for p in code_paths:
    lang = p.suffix.lstrip(".") or "plaintext"
    code = html.escape(p.read_text(encoding="utf-8"))
    rel = p.relative_to(ROOT)
    code_parts.append(
      f"""
<section class=\"code-block\">
  <div class=\"code-head\">
    <h3>{html.escape(p.name)}</h3>
    <span class=\"path\">{html.escape(str(rel))}</span>
  </div>
  <pre><code class=\"language-{lang}\">{code}</code></pre>
</section>
"""
    )

  if not code_parts:
    code_parts.append("<p>未找到对应代码文件。</p>")

  body = f"""
<div class=\"layout\">
  <section class=\"panel left\">
    <div class=\"topbar\">
      <a class=\"back\" href=\"./index.html\">返回主页</a>
      <span class=\"badge\">题号 {html.escape(idx)}</span>
    </div>
    <h1>{html.escape(q_title)}</h1>
    {q_html}
  </section>
  <section class=\"panel right\">
    <h2>代码实现</h2>
    <p class=\"code-intro\">对应题解代码与测试文件按目录展示，便于对照阅读与回顾。</p>
    {''.join(code_parts)}
  </section>
</div>
"""
  return page_shell(f"题目 {idx} - {q_title}", body)


def build_home_page(items: List[Tuple[str, Path, List[Path]]]) -> str:
  cards = []
  for idx, q_path, code_paths in items:
    title = nice_title(q_path)
    cards.append(
      f"""
<a class=\"card\" href=\"./problem-{html.escape(idx)}.html\">
  <div class=\"card-id\">题号 {html.escape(idx)}</div>
  <div class=\"card-title\">{html.escape(title)}</div>
  <div class=\"card-meta\">{len(code_paths)} 个代码文件</div>
</a>
"""
    )

  body = f"""
<main class=\"home-wrap\">
  <section class=\"hero\">
    <span class=\"eyebrow\">ALGORITHM NOTEBOOK</span>
    <h1 class=\"home-title\">算法题与实例代码</h1>
    <p class=\"home-sub\">点击卡片进入详情页，左侧为题目说明，右侧为代码实现与测试。页面支持语法高亮，适合直接复盘每道题的思路和落地代码。</p>
  </section>
  <section class=\"grid\">
    {''.join(cards) if cards else '<p>未发现题目文件。</p>'}
  </section>
</main>
"""
  return page_shell("题目主页", body)


def main() -> None:
  OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

  questions, code_map = collect_files()
  all_ids = sorted(set(questions.keys()) | set(code_map.keys()), key=lambda x: (not x.isdigit(), int(x) if x.isdigit() else x))

  items: List[Tuple[str, Path, List[Path]]] = []
  for idx in all_ids:
    q_path = questions.get(idx)
    if q_path is None:
      continue
    code_paths = code_map.get(idx, [])
    html_text = build_problem_page(idx, q_path, code_paths)
    (OUTPUT_DIR / f"problem-{idx}.html").write_text(html_text, encoding="utf-8")
    items.append((idx, q_path, code_paths))

  home = build_home_page(items)
  (OUTPUT_DIR / "index.html").write_text(home, encoding="utf-8")
  print(f"Generated {len(items)} problem pages at: {OUTPUT_DIR}")


if __name__ == "__main__":
  main()
