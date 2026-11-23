"""QR-Code für eine Einheit. Aufruf: python3 _tools/qr.py gams/kl8-thema/ "Titel"
Erzeugt _qr/<ordnername>.svg und _qr/<ordnername>.html (A4-Plakat; wenn Playwright+Chrome da sind, auch .pdf)."""
import os, sys
from reportlab.graphics.barcode.qr import QrCodeWidget
BASE = "https://mythosymbolum.github.io/unterricht/"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def qr_svg(url):
    w = QrCodeWidget(url, barLevel="M"); w.draw(); q = w.qr; n = q.getModuleCount()
    r = "".join(f'<rect x="{c}" y="{y}" width="1.02" height="1.02"/>' for y in range(n) for c in range(n) if q.isDark(y, c))
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-4 -4 {n+8} {n+8}" shape-rendering="crispEdges"><rect x="-4" y="-4" width="{n+8}" height="{n+8}" fill="#fff"/><g fill="#000">{r}</g></svg>'

if __name__ == "__main__":
    path = sys.argv[1].strip("/") + "/" if len(sys.argv) > 1 and sys.argv[1].strip("/") else ""
    title = sys.argv[2] if len(sys.argv) > 2 else "Religionsunterricht"
    url = BASE + path
    name = path.strip("/").replace("/", "_") or "startseite"
    out = os.path.join(os.getcwd(), "qr_out"); os.makedirs(out, exist_ok=True)
    svg = qr_svg(url)
    open(f"{out}/{name}.svg", "w").write(svg)
    font = "file://" + os.path.join(ROOT, "_tools", "fonts", "ComicRelief-Bold.ttf")
    html = f'''<!DOCTYPE html><html><head><meta charset="utf-8"><style>@page{{size:A4;margin:0}}
@font-face{{font-family:CR;src:url({font})}}body{{margin:0;font-family:CR,sans-serif;text-align:center;color:#2d2a26}}
.p{{width:210mm;height:297mm;padding:25mm 20mm}}h1{{font-size:30pt;margin:0 0 6mm}}p{{font-size:20pt}}.q{{width:140mm;height:140mm;margin:10mm auto}}
small{{font-size:13pt}}</style></head><body><div class="p"><h1>{title}</h1><p>Scanne den Code mit deinem iPad!</p>
<div class="q">{svg}</div><small>{url}</small></div></body></html>'''
    open(f"{out}/{name}.html", "w").write(html)
    try:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            exe = next((e for e in ["/usr/bin/google-chrome", "/usr/bin/chromium"] if os.path.exists(e)), None)
            b = p.chromium.launch(executable_path=exe) if exe else p.chromium.launch()
            pg = b.new_page(); pg.goto(f"file://{out}/{name}.html"); pg.wait_for_timeout(300)
            pg.pdf(path=f"{out}/{name}.pdf", format="A4", print_background=True, prefer_css_page_size=True); b.close()
        print("PDF:", f"{out}/{name}.pdf")
    except Exception as e:
        print("Kein PDF (", e, ") – HTML/SVG liegen in", out)
    print("URL:", url)
