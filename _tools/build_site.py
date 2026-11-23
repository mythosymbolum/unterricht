"""Baut index.html (Startseite) aus lessons.json. Aufruf: python3 _tools/build_site.py"""
import base64, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import illus as I

FONT = os.path.join(HERE, "fonts") + "/"
b64 = lambda p: base64.b64encode(open(p, "rb").read()).decode()

LESSONS = [(l["path"], l["schule"], l["klasse"], l["titel"], l["untertitel"], l.get("icon", "kreuz"))
           for l in json.load(open(os.path.join(ROOT, "lessons.json"), encoding="utf-8"))]
# Sortierung: Schule, dann Klasse
LESSONS.sort(key=lambda l: (l[1], int("".join(c for c in l[2] if c.isdigit()) or 0)))

tiles = ""
for path, school, kl, title, sub, ic in LESSONS:
    tiles += f'''<a class="tile" href="{path}" data-s="{school}"><div class="ic">{I.obj(ic, "t" + ic)}</div>
<div><div class="meta">{school} · Klasse {kl}</div><h2>{title}</h2><p>{sub}</p></div></a>'''
schools = sorted({l[1] for l in LESSONS})
filt = '<button class="f on" data-s="">Alle</button>' + "".join(f'<button class="f" data-s="{s}">{s}</button>' for s in schools)

html = f'''<!DOCTYPE html><html lang="de"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Religionsunterricht · Materialien</title>
<style>
@font-face{{font-family:CR;src:url(data:font/ttf;base64,{b64(FONT+"ComicRelief-Regular.ttf")}) format("truetype")}}
@font-face{{font-family:CR;src:url(data:font/ttf;base64,{b64(FONT+"ComicRelief-Bold.ttf")}) format("truetype");font-weight:700}}
*{{box-sizing:border-box}}
body{{margin:0;font-family:CR,"Comic Sans MS",sans-serif;color:#2d2a26;background:#fbf6ec;
 background-image:radial-gradient(#efe4cf 1px,transparent 1px);background-size:22px 22px;min-height:100vh}}
header{{background:#f3e6cc;border-bottom:3px solid #2d2a26;padding:22px 28px}}
header h1{{margin:0;font-size:clamp(28px,5vw,44px)}}header p{{margin:4px 0 0;font-size:19px;color:#5d554c}}
main{{max-width:1100px;margin:0 auto;padding:22px 20px 40px}}
.filters{{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:18px}}
.f{{font:inherit;font-size:19px;font-weight:700;border:3px solid #2d2a26;border-radius:30px;background:#fff;padding:6px 20px;cursor:pointer}}.f.on{{background:#2d2a26;color:#fff}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:18px}}
.tile{{display:flex;gap:16px;align-items:center;background:#fff;border:3px solid #2d2a26;border-radius:18px;padding:14px 18px;
 box-shadow:5px 5px 0 #2d2a26;color:inherit;text-decoration:none;transition:transform .15s}}
.tile:active,.tile:hover{{transform:translate(-2px,-2px);box-shadow:7px 7px 0 #2d2a26}}
.ic{{width:84px;height:84px;flex:none}}.ic svg{{width:100%;height:100%}}
.meta{{font-size:15px;color:#c8553d;font-weight:700;letter-spacing:.04em;text-transform:uppercase}}
.tile h2{{margin:2px 0 4px;font-size:23px;line-height:1.15}}.tile p{{margin:0;font-size:16px;color:#5d554c}}
.tile.hide{{display:none}}
footer{{text-align:center;font-size:14px;color:#8a7c67;padding:10px}}
</style></head><body>
<header><h1>Religionsunterricht</h1><p>Interaktive Präsentationen – tippe auf dein Thema!</p></header>
<main><div class="filters">{filt}</div><div class="grid">{tiles}</div></main>
<footer>Katholische Religionslehre · Schuljahr 2026/27</footer>
<script>
document.querySelectorAll('.f').forEach(b=>b.onclick=()=>{{document.querySelectorAll('.f').forEach(x=>x.classList.toggle('on',x===b));
 document.querySelectorAll('.tile').forEach(t=>t.classList.toggle('hide',!!b.dataset.s&&t.dataset.s!==b.dataset.s))}});
</script></body></html>'''
open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(html)
print("ok")
