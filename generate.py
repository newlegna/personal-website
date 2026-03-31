import os, re
try:
    import markdown
except ImportError:
    os.system("pip3 install markdown")
    import markdown

base_dir = "/Users/angel/Desktop/notion-export/Things-I’m-working-on/Getting-a-job-Work-life/Angel’s-UX-Portfolio/Untitled"
out_dir = "/Users/angel/Documents/GitHub/personal-website"

files = [
    ("Nomad-Project/Nomad-Project.md", "nomad.html", "Nomad Project"),
    ("nwhacks/nwhacks.md", "nwhacks.html", "nwHacks"),
    ("Radical-hospitality/Radical-hospitality.md", "radical-hospitality.html", "Radical Hospitality"),
    ("AIC/AIC.md", "aic.html", "Accommodation in Canada")
]

template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} — Angel Wen</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Space+Mono:wght@400&family=Playfair+Display:ital,wght@0,400;0,500;0,600;1,400;1,500&display=swap" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        :root {
            --bg: #0a0a0a; --text-main: #f2f2f2; --text-muted: #888888;
            --border: rgba(255, 255, 255, 0.08);
            --font-sans: 'Inter', sans-serif; --font-serif: 'Playfair Display', serif; --font-mono: 'Space Mono', monospace;
        }
        body { font-family: var(--font-sans); color: var(--text-main); background: var(--bg); line-height: 1.6; -webkit-font-smoothing: antialiased; }
        a { color: inherit; text-decoration: none; }
        .header { padding: 2rem 4vw; display: flex; justify-content: space-between; align-items: center; position: sticky; top: 0; background: rgba(10,10,10,0.9); backdrop-filter: blur(10px); z-index: 100;}
        .logo { font-weight: 500; }
        .nav-link { font-size: 0.875rem; padding-bottom: 2px; border-bottom: 1px solid var(--text-muted); transition: color 0.3s; color: var(--text-muted);}
        .nav-link:hover { color: var(--text-main); border-color: var(--text-main);}
        .container { max-width: 760px; margin: 0 auto; padding: 2rem 4vw 8rem; }
        .case-study img { width: 100%; height: auto; border-radius: 4px; margin: 3rem 0; }
        .case-study h1 { font-family: var(--font-serif); font-size: clamp(2.5rem, 5vw, 3.5rem); font-weight: 400; margin-bottom: 1rem; line-height: 1.1; letter-spacing: -0.02em; }
        .case-study h2 { font-family: var(--font-serif); font-size: 2rem; font-weight: 400; margin-top: 5rem; margin-bottom: 1.5rem; color: var(--text-main); }
        .case-study h3 { font-size: 1.25rem; font-weight: 500; margin-top: 3rem; margin-bottom: 1rem; color: var(--text-main); }
        .case-study p { margin-bottom: 1.5rem; color: var(--text-muted); font-size: 1.125rem; }
        .case-study ul { margin-bottom: 1.5rem; padding-left: 2rem; color: var(--text-muted); font-size: 1.125rem; }
        .case-study li { margin-bottom: 0.5rem; }
        .case-study blockquote { border-left: 2px solid var(--border); padding-left: 2rem; margin: 3rem 0; font-style: italic; font-size: 1.25rem; color: var(--text-main); }
        .footer { text-align: center; padding: 4rem 0; border-top: 1px solid var(--border); margin-top: 4rem; color: var(--text-muted); font-size: 0.875rem; }
        @media (max-width: 768px) {
            .header { padding: 1.25rem 4vw; }
            .container { padding: 1.5rem 4vw 4rem; }
            .case-study h1 { font-size: 2rem; }
            .case-study h2 { font-size: 1.5rem; margin-top: 3rem; margin-bottom: 1rem; }
            .case-study h3 { margin-top: 2rem; }
            .case-study p, .case-study ul { font-size: 1rem; }
            .case-study img { margin: 1.5rem 0; }
            .case-study blockquote { margin: 2rem 0; font-size: 1.1rem; padding-left: 1rem; }
        }
    </style>
</head>
<body>
    <header class="header">
        <a href="index.html" class="logo">Angel Wen</a>
        <a href="index.html" class="nav-link">Back to Work</a>
    </header>
    <main class="container case-study">
        {content}
    </main>
    <footer class="footer container">
        <a href="index.html" class="nav-link">← Return to Portfolio</a>
    </footer>
</body>
</html>"""

for md_path, out_file, title in files:
    full_path = os.path.join(base_dir, md_path)
    if not os.path.exists(full_path):
        continue
    with open(full_path, "r") as f:
        content = f.read()
    
    # Clean up markdown
    content = re.sub(r'(?s)^---.*?---', '', content)
    content = content.replace("./assets/", "assets/")
    content = re.sub(r'- \[Untitled\]\(.*?\)', '', content)
    
    html_content = markdown.markdown(content)
    final_html = template.replace("{title}", title).replace("{content}", html_content)
    
    with open(os.path.join(out_dir, out_file), "w") as f:
        f.write(final_html)

