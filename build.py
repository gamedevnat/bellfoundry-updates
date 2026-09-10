#!/usr/bin/env python3
"""Render the public files into site/, which is what Pages serves.

version.json is the file the app reads and is copied verbatim — it is a
contract, not a document, and nothing here may reformat it.

privacy.md is rendered to HTML because a Chrome Web Store reviewer opens the
URL in a browser, and raw markdown served as text/plain reads as a broken
link rather than as a policy.
"""
import json
import shutil
from pathlib import Path

import markdown

ROOT = Path(__file__).parent
SITE = ROOT / "site"
SITE.mkdir(exist_ok=True)

# The app reads this. Copy it exactly.
shutil.copyfile(ROOT / "version.json", SITE / "version.json")
version = json.loads((ROOT / "version.json").read_text())["version"]

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>
  :root {{ color-scheme: light dark; --ink:#1f1a24; --paper:#ece5da; --rule:#b9b3bd; --dim:#5c5566; }}
  @media (prefers-color-scheme: dark) {{
    :root {{ --ink:#ece5da; --paper:#1f1a24; --rule:#3a3342; --dim:#b9b3bd; }}
  }}
  body {{ margin:0; background:var(--paper); color:var(--ink);
         font:16px/1.6 ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif; }}
  main {{ max-width:44rem; margin:0 auto; padding:3rem 1.25rem 5rem; }}
  h1 {{ font-size:1.75rem; line-height:1.2; margin:0 0 .25rem; }}
  h2 {{ font-size:1.15rem; margin:2.25rem 0 .5rem; }}
  table {{ border-collapse:collapse; width:100%; display:block; overflow-x:auto; }}
  th,td {{ text-align:left; padding:.5rem .75rem .5rem 0; border-bottom:1px solid var(--rule);
           vertical-align:top; }}
  code {{ font-size:.9em; }}
  hr {{ border:0; border-top:1px solid var(--rule); margin:2.5rem 0 1.25rem; }}
  a {{ color:inherit; }}
  .sub {{ color:var(--dim); margin:0 0 2rem; }}
</style>
</head>
<body><main>
{body}
</main></body>
</html>
"""

md = markdown.Markdown(extensions=["tables", "attr_list"])
html = md.convert((ROOT / "privacy.md").read_text())
(SITE / "privacy.html").write_text(PAGE.format(title="Privacy policy — Bellfoundry extension", body=html))

index = f"""<h1>bellfoundry-updates</h1>
<p class="sub">Two small public files for
<a href="https://connectioneering.itch.io/bellfoundry">Bellfoundry</a>,
whose own repository is private.</p>
<table>
<tr><th>File</th><th>Read by</th></tr>
<tr><td><a href="version.json">version.json</a></td>
    <td>The app's <b>Check for updates</b> button. Currently names {version}.</td></tr>
<tr><td><a href="privacy.html">privacy.html</a></td>
    <td>The browser-extension privacy policy.</td></tr>
</table>
<p>Nothing here is downloaded automatically. <code>version.json</code> is
fetched only when somebody presses the button, and all it does is name a
version and a store page to open by hand.</p>
<hr>
<p class="sub">Bellfoundry is not affiliated with or endorsed by Anthropic.</p>"""
(SITE / "index.html").write_text(PAGE.format(title="bellfoundry-updates", body=index))

print(f"site/: version.json ({version}), privacy.html, index.html")
