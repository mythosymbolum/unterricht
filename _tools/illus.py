"""Gemeinsame SVG-Illustrationen im Skizzenstil für Präsentation und Arbeitsblätter."""

INK = "#2d2a26"
PAPER = "#fbf6ec"
RED = "#c8553d"
GOLD = "#e0a526"
BLUE = "#3d6e9e"
GREEN = "#5c8f4e"
VIOLET = "#7a5c99"
STONE = "#d9cdb8"
STONE2 = "#c9b99c"
WOOD = "#b98a5a"
LIGHTWOOD = "#e3c79f"


def defs(uid="r"):
    """Filter für handgezeichnete Linien + Schraffur-Muster."""
    return f'''<defs>
<filter id="{uid}rough" x="-5%" y="-5%" width="110%" height="110%">
 <feTurbulence type="fractalNoise" baseFrequency="0.035" numOctaves="2" seed="7" result="n"/>
 <feDisplacementMap in="SourceGraphic" in2="n" scale="2.6" xChannelSelector="R" yChannelSelector="G"/>
</filter>
<pattern id="{uid}hatch" width="9" height="9" patternUnits="userSpaceOnUse" patternTransform="rotate(40)">
 <line x1="0" y1="0" x2="0" y2="9" stroke="{INK}" stroke-width="1" opacity=".25"/>
</pattern>
<pattern id="{uid}floor" width="40" height="40" patternUnits="userSpaceOnUse">
 <rect width="40" height="40" fill="#f3ead8"/>
 <path d="M0 0H40M0 0V40" stroke="#e0d3ba" stroke-width="1.2"/>
</pattern>
</defs>'''


def svg(inner, vb="0 0 200 200", uid="r", cls="", extra="", top=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" class="{cls}" {extra}>'
            f'{defs(uid)}<g filter="url(#{uid}rough)" stroke="{INK}" stroke-width="3.2" '
            f'stroke-linecap="round" stroke-linejoin="round">{inner}</g>'
            f'<g stroke="{INK}" stroke-width="2.6" font-family="Comic Relief, Comic Sans MS, sans-serif">{top}</g></svg>')


# ---------------------------------------------------------------- Gegenstände
def g_kelch(u="r"):
    return f'''
<path d="M62 40 H138 C138 88 120 108 100 112 C80 108 62 88 62 40Z" fill="{GOLD}"/>
<path d="M66 52 H134" stroke-width="2" opacity=".6"/>
<path d="M100 112 V150" stroke-width="7"/><path d="M100 112 V150" stroke="{GOLD}" stroke-width="3"/>
<ellipse cx="100" cy="132" rx="12" ry="7" fill="{GOLD}"/>
<path d="M64 168 C70 152 130 152 136 168 Z" fill="{GOLD}"/>
<path d="M80 72 C84 92 92 100 100 102" fill="none" stroke="#fff" stroke-width="3" opacity=".7"/>'''


def g_hostienschale(u="r"):
    return f'''
<ellipse cx="100" cy="118" rx="72" ry="22" fill="{GOLD}"/>
<path d="M28 118 C34 150 166 150 172 118" fill="{GOLD}"/>
<path d="M78 146 L72 170 H128 L122 146" fill="{GOLD}"/>
<ellipse cx="100" cy="110" rx="34" ry="11" fill="#fffdf6"/>
<ellipse cx="72" cy="114" rx="16" ry="6" fill="#fffdf6"/>
<ellipse cx="128" cy="114" rx="16" ry="6" fill="#fffdf6"/>
<path d="M100 80 V100 M92 90 H108" stroke-width="2.4"/>'''


def g_weihrauch(u="r"):
    return f'''
<path d="M100 14 V60" stroke-width="2"/><path d="M80 18 L70 92 M120 18 L130 92" stroke-width="2"/>
<circle cx="100" cy="14" r="7" fill="{GOLD}"/>
<path d="M70 92 H130 C134 112 126 128 100 132 C74 128 66 112 70 92Z" fill="{GOLD}"/>
<path d="M76 92 C80 70 120 70 124 92" fill="{GOLD}"/>
<path d="M90 80 h6 M104 80 h6" stroke-width="2"/>
<path d="M88 132 L84 146 H116 L112 132" fill="{GOLD}"/>
<path d="M140 70 C156 60 142 48 156 38 C168 30 158 18 170 10" fill="none" stroke-width="2.4" opacity=".6"/>
<path d="M150 96 C166 86 152 74 168 64" fill="none" stroke-width="2.4" opacity=".5"/>'''


def g_osterkerze(u="r"):
    return f'''
<path d="M100 18 C88 34 92 48 100 52 C108 48 112 34 100 18Z" fill="{GOLD}"/>
<path d="M100 30 C96 38 98 46 100 48" fill="none" stroke="{RED}" stroke-width="2"/>
<path d="M100 52 V62" stroke-width="2"/>
<rect x="78" y="62" width="44" height="110" rx="3" fill="#fffaf0"/>
<path d="M100 76 V128 M84 96 H116" stroke="{RED}" stroke-width="4"/>
<text x="84" y="90" font-family="serif" font-size="14" fill="{RED}" stroke="none">A</text>
<text x="105" y="140" font-family="serif" font-size="14" fill="{RED}" stroke="none">Ω</text>
<circle cx="100" cy="86" r="2.5" fill="{RED}" stroke="none"/><circle cx="100" cy="118" r="2.5" fill="{RED}" stroke="none"/>
<circle cx="90" cy="96" r="2.5" fill="{RED}" stroke="none"/><circle cx="110" cy="96" r="2.5" fill="{RED}" stroke="none"/>
<circle cx="100" cy="96" r="2.5" fill="{RED}" stroke="none"/>
<text x="82" y="160" font-family="sans-serif" font-size="11" fill="{INK}" stroke="none">2 0 2 6</text>
<path d="M66 172 H134 L126 186 H74Z" fill="{GOLD}"/>'''


def g_ewigeslicht(u="r"):
    return f'''
<path d="M100 8 V40" stroke-width="2"/>
<path d="M100 40 L76 70 M100 40 L124 70" stroke-width="2"/>
<path d="M70 70 H130 L122 140 C118 156 82 156 78 140Z" fill="{RED}"/>
<path d="M74 84 H126" stroke-width="2" opacity=".5"/>
<ellipse cx="100" cy="108" rx="14" ry="20" fill="#ffd36b" stroke-width="2"/>
<path d="M100 96 C95 104 96 114 100 118 C104 114 105 104 100 96Z" fill="#fff4c2" stroke-width="1.6"/>
<path d="M92 154 L100 170 L108 154" fill="{GOLD}"/>'''


def g_tabernakel(u="r"):
    return f'''
<path d="M50 70 L100 32 L150 70Z" fill="{GOLD}"/>
<rect x="56" y="70" width="88" height="90" fill="{GOLD}"/>
<rect x="72" y="84" width="56" height="62" rx="4" fill="#f5d77e"/>
<path d="M100 84 V146" stroke-width="2.4"/>
<circle cx="94" cy="116" r="3" fill="{INK}"/><circle cx="106" cy="116" r="3" fill="{INK}"/>
<path d="M86 100 H114 M100 92 V108" stroke="{RED}" stroke-width="2.4" transform="translate(0,-2) scale(1)" opacity="0"/>
<rect x="46" y="160" width="108" height="14" fill="{LIGHTWOOD}"/>
<path d="M100 20 V42 M92 28 H108" stroke-width="2.4"/>'''


def g_taufbecken(u="r"):
    return f'''
<path d="M38 70 H162 L150 112 H50Z" fill="{STONE}"/>
<ellipse cx="100" cy="70" rx="62" ry="12" fill="#9fc6e4"/>
<path d="M72 112 H128 L122 160 H78Z" fill="{STONE}"/>
<path d="M60 160 H140 V176 H60Z" fill="{STONE2}"/>
<path d="M84 66 C92 62 108 62 116 66" fill="none" stroke="#fff" stroke-width="2.4"/>
<path d="M100 18 C92 30 92 38 100 42 C108 38 108 30 100 18Z" fill="#9fc6e4" stroke-width="2.4"/>
<path d="M70 86 C80 94 92 86 100 94 C108 86 120 94 130 86" fill="none" stroke-width="2" opacity=".5"/>'''


def g_weihwasser(u="r"):
    return f'''
<path d="M60 40 H140 V54 H60Z" fill="{STONE2}"/>
<path d="M66 54 V150" stroke-width="2" opacity=".35"/><path d="M134 54 V150" stroke-width="2" opacity=".35"/>
<path d="M54 92 H146 C144 132 124 146 100 146 C76 146 56 132 54 92Z" fill="{STONE}"/>
<ellipse cx="100" cy="92" rx="46" ry="9" fill="#9fc6e4"/>
<path d="M100 146 V170" stroke-width="5"/>
<path d="M150 50 C156 58 154 66 150 70 C146 66 144 58 150 50Z" fill="#9fc6e4" stroke-width="2"/>
<path d="M162 70 C166 76 165 82 162 84 C159 82 158 76 162 70Z" fill="#9fc6e4" stroke-width="2"/>'''


def g_ambo(u="r"):
    return f'''
<path d="M52 52 L148 40 L144 64 L56 72Z" fill="{LIGHTWOOD}"/>
<path d="M66 50 L96 46 L100 60 L70 64Z M104 45 L134 41 L136 56 L106 59Z" fill="#fffaf0" stroke-width="2"/>
<path d="M70 72 H130 L122 168 H78Z" fill="{WOOD}"/>
<path d="M88 96 H112 M100 84 V120" stroke="{GOLD}" stroke-width="5"/>
<path d="M60 168 H140 V180 H60Z" fill="{LIGHTWOOD}"/>'''


def g_altar(u="r"):
    return f'''
<rect x="26" y="78" width="148" height="18" fill="#fffaf0"/>
<path d="M26 96 H174 V108 H26Z" fill="#fffaf0"/>
<rect x="38" y="96" width="124" height="74" fill="{STONE}"/>
<path d="M100 112 V156 M84 128 H116" stroke="{RED}" stroke-width="5"/>
<rect x="28" y="170" width="144" height="12" fill="{STONE2}"/>
<path d="M56 78 V54" stroke-width="3"/><path d="M56 40 C52 46 53 52 56 54 C59 52 60 46 56 40Z" fill="{GOLD}" stroke-width="2"/>
<path d="M144 78 V54" stroke-width="3"/><path d="M144 40 C140 46 141 52 144 54 C147 52 148 46 144 40Z" fill="{GOLD}" stroke-width="2"/>'''


def g_kreuz(u="r"):
    return f'''
<path d="M88 16 H112 V60 H156 V84 H112 V184 H88 V84 H44 V60 H88Z" fill="{WOOD}"/>
<path d="M100 66 C96 72 96 96 100 120 C104 96 104 72 100 66Z" fill="{LIGHTWOOD}" stroke-width="2"/>
<path d="M64 70 C80 74 92 74 100 72 C108 74 120 74 136 70" fill="none" stroke-width="3"/>
<circle cx="100" cy="60" r="7" fill="{LIGHTWOOD}" stroke-width="2"/>
<rect x="90" y="24" width="20" height="12" fill="#fffaf0" stroke-width="1.6"/>
<text x="92" y="34" font-size="8" font-family="serif" stroke="none" fill="{INK}">INRI</text>'''


def g_orgel(u="r"):
    pipes = ""
    hs = [70, 90, 112, 130, 140, 130, 112, 90, 70]
    for i, h in enumerate(hs):
        x = 34 + i * 15
        pipes += f'<path d="M{x} {150-h} h11 v{h} h-11Z" fill="#e8e3da"/><path d="M{x} {150-h+h*0.75} l5.5 -6 l5.5 6" fill="none" stroke-width="1.6"/>'
    return f'''<rect x="26" y="146" width="148" height="34" fill="{WOOD}"/>{pipes}
<path d="M40 162 H160" stroke-width="2"/><path d="M50 162 v10 M64 162 v10 M78 162 v10 M92 162 v10 M106 162 v10 M120 162 v10 M134 162 v10 M148 162 v10" stroke-width="1.5"/>'''


def g_beichtstuhl(u="r"):
    return f'''
<path d="M30 60 L100 26 L170 60Z" fill="{WOOD}"/>
<rect x="30" y="60" width="140" height="120" fill="{LIGHTWOOD}"/>
<rect x="76" y="74" width="48" height="106" fill="{WOOD}"/>
<path d="M40 74 H70 V180 H40Z M130 74 H160 V180 H130Z" fill="none" stroke-width="2.4"/>
<path d="M40 74 C55 90 55 110 40 120 M160 74 C145 90 145 110 160 120" fill="#9b4a3a" stroke-width="2"/>
<path d="M88 90 h24 v30 h-24Z" fill="none" stroke-width="2"/><path d="M94 90 v30 M100 90 v30 M106 90 v30" stroke-width="1.4"/>'''


def g_glocke(u="r"):
    return f'''
<path d="M100 18 V30" stroke-width="5"/>
<path d="M72 42 C72 34 128 34 128 42 C130 80 136 112 156 140 H44 C64 112 70 80 72 42Z" fill="{GOLD}"/>
<path d="M40 140 H160 C160 150 40 150 40 140Z" fill="{GOLD}"/>
<circle cx="100" cy="160" r="10" fill="{GOLD}"/><path d="M100 140 V150" stroke-width="3"/>
<path d="M82 60 C80 84 78 104 70 124" fill="none" stroke="#fff" stroke-width="3" opacity=".7"/>
<path d="M30 70 C20 80 20 100 30 110 M170 70 C180 80 180 100 170 110 M18 60 C2 80 2 100 18 120 M182 60 C198 80 198 100 182 120" fill="none" stroke-width="2.4" opacity=".6"/>'''


def g_lektionar(u="r"):
    return f'''
<path d="M100 54 C80 40 46 38 22 44 V160 C46 154 80 156 100 170 C120 156 154 154 178 160 V44 C154 38 120 40 100 54Z" fill="#fffaf0"/>
<path d="M100 54 V170" stroke-width="2.4"/>
<path d="M36 70 H86 M36 86 H86 M36 102 H80 M36 118 H86 M36 134 H76 M114 70 H164 M114 86 H160 M114 102 H164 M114 118 H156 M114 134 H164" stroke-width="2" opacity=".45"/>
<path d="M100 170 V190" stroke="{RED}" stroke-width="4"/>
'''


def g_kreuzweg(u="r"):
    return f'''
<rect x="38" y="30" width="124" height="140" rx="6" fill="{LIGHTWOOD}"/>
<rect x="50" y="42" width="100" height="100" fill="#f4ecdc"/>
<path d="M116 52 L84 132" stroke="{WOOD}" stroke-width="9"/><path d="M78 74 L132 96" stroke="{WOOD}" stroke-width="9"/>
<circle cx="80" cy="84" r="9" fill="{LIGHTWOOD}" stroke-width="2.4"/>
<path d="M80 93 C74 104 72 118 76 134 M80 100 L96 90" fill="none" stroke-width="2.4"/>
<text x="88" y="162" font-size="16" font-family="serif" stroke="none" fill="{INK}">VII</text>'''


def g_kirchturm(u="r"):
    return f'''
<path d="M100 8 V28 M92 16 H108" stroke-width="3"/>
<path d="M100 28 L70 92 H130Z" fill="#7a9cbc"/>
<rect x="70" y="92" width="60" height="96" fill="{STONE}"/>
<path d="M88 110 C88 100 112 100 112 110 V128 H88Z" fill="#5b4b3a"/>
<circle cx="100" cy="150" r="12" fill="#fffaf0" stroke-width="2.4"/><path d="M100 150 V142 M100 150 H106" stroke-width="2"/>
<path d="M90 188 V170 C90 162 110 162 110 188" fill="{WOOD}"/>'''


OBJECTS = {
    "kelch": ("Kelch", g_kelch),
    "hostienschale": ("Hostienschale", g_hostienschale),
    "weihrauch": ("Weihrauchfass", g_weihrauch),
    "osterkerze": ("Osterkerze", g_osterkerze),
    "ewigeslicht": ("Ewiges Licht", g_ewigeslicht),
    "tabernakel": ("Tabernakel", g_tabernakel),
    "taufbecken": ("Taufbecken", g_taufbecken),
    "weihwasser": ("Weihwasserbecken", g_weihwasser),
    "ambo": ("Ambo", g_ambo),
    "altar": ("Altar", g_altar),
    "kreuz": ("Kreuz", g_kreuz),
    "orgel": ("Orgel", g_orgel),
    "beichtstuhl": ("Beichtstuhl", g_beichtstuhl),
    "glocke": ("Glocken", g_glocke),
    "lektionar": ("Lektionar", g_lektionar),
    "kreuzweg": ("Kreuzweg", g_kreuzweg),
    "kirchturm": ("Kirchturm", g_kirchturm),
}


def obj(key, uid=None, cls="obj"):
    uid = uid or key
    return svg(OBJECTS[key][1](uid), uid=uid, cls=cls)


# --------------------------------------------------------- Grundriss der Kirche
# Positionen (viewBox 0 0 600 880) – Altar im Osten (oben), Eingang im Westen (unten)
PLAN_SPOTS = {
    "tabernakel": (300, 56),
    "ewigeslicht": (352, 62),
    "kreuz": (300, 118),
    "altar": (300, 178),
    "ambo": (228, 228),
    "osterkerze": (372, 228),
    "beichtstuhl": (108, 308),
    "marienaltar": (492, 308),
    "kreuzweg": (196, 470),
    "baenke": (300, 520),
    "taufbecken": (232, 690),
    "orgel": (368, 690),
    "weihwasser": (262, 748),
    "kirchturm": (300, 820),
}


def church_plan(uid="plan", numbers=None, show_icons=True):
    """numbers: dict key->Zahl für nummerierte Kreise (für Beschriftungsaufgaben)."""
    s = []
    # Außenmauer (Kreuzform + Apsis + Turm)
    s.append(f'''<path d="M200 120 A100 100 0 0 1 400 120 V255 H540 V360 H410 V760 H345 V860 H255 V760 H190 V360 H60 V255 H200 Z"
      fill="url(#{uid}floor)" stroke-width="9"/>''')
    # Altarraum leicht erhöht
    s.append(f'<path d="M205 252 V122 A95 95 0 0 1 395 122 V252Z" fill="#efe1c4" stroke="none"/>')
    s.append('<path d="M200 255 H400" stroke-width="2.5" stroke-dasharray="10 6"/>')
    s.append('<path d="M214 264 H386" stroke-width="1.8" opacity=".5"/>')
    # Bänke
    for i in range(9):
        y = 395 + i * 28
        s.append(f'<rect x="212" y="{y}" width="70" height="14" rx="2" fill="{LIGHTWOOD}" stroke-width="2"/>')
        s.append(f'<rect x="318" y="{y}" width="70" height="14" rx="2" fill="{LIGHTWOOD}" stroke-width="2"/>')
    # Kreuzweg-Stationen an den Wänden
    for i in range(7):
        y = 395 + i * 40
        s.append(f'<path d="M190 {y} h10 M195 {y-5} v10" stroke-width="2"/><path d="M405 {y} h10 M410 {y-5} v10" stroke-width="2"/>')
    # Tür
    s.append(f'<path d="M278 860 H322" stroke="{PAPER}" stroke-width="12"/><path d="M278 860 A22 22 0 0 1 300 838 M322 860 A22 22 0 0 0 300 838" fill="none" stroke-width="2" opacity=".6"/>')
    # Turm-Durchgang
    s.append(f'<path d="M262 760 H338" stroke="{PAPER}" stroke-width="10"/>')
    if show_icons:
        def mini(key, x, y, sc=0.32):
            f = OBJECTS[key][1](uid)
            return f'<g transform="translate({x-100*sc},{y-100*sc}) scale({sc})" stroke-width="5">{f}</g>'
        s.append(mini("tabernakel", 300, 56, .26))
        s.append(mini("ewigeslicht", 352, 62, .22))
        s.append(mini("kreuz", 300, 118, .24))
        s.append(mini("altar", 300, 182, .34))
        s.append(mini("ambo", 228, 228, .26))
        s.append(mini("osterkerze", 372, 228, .26))
        s.append(mini("beichtstuhl", 108, 308, .32))
        s.append(f'<g transform="translate(492,308)"><rect x="-30" y="-16" width="60" height="24" fill="{STONE}" stroke-width="2.4"/>'
                 f'<path d="M-6 -34 C-10 -26 -8 -18 0 -16 C8 -18 10 -26 6 -34 C4 -40 -4 -40 -6 -34Z" fill="#8fb3d9" stroke-width="2"/>'
                 + "".join(f'<path d="M{-24+i*10} 18 v-8" stroke="{GOLD}" stroke-width="5"/>' for i in range(6)) + '</g>')
        s.append(mini("taufbecken", 232, 690, .3))
        s.append(mini("orgel", 368, 690, .3))
        s.append(mini("weihwasser", 262, 748, .18))
        s.append(mini("weihwasser", 338, 748, .18))
        s.append(mini("glocke", 300, 812, .3))
    t = []
    if numbers:
        for key, n in numbers.items():
            x, y = PLAN_SPOTS[key]
            t.append(f'<g class="num" data-key="{key}"><circle cx="{x+30}" cy="{y-22}" r="17" fill="#fff" stroke-width="2.6"/>'
                     f'<text x="{x+30}" y="{y-15}" text-anchor="middle" font-size="20" font-weight="700" stroke="none" fill="{INK}">{n}</text></g>')
    # Himmelsrichtung
    t.append('<g transform="translate(548,60)"><path d="M0 26 V-14 M-8 -4 L0 -16 L8 -4" fill="none" stroke-width="2.4"/>'
             f'<text x="0" y="44" text-anchor="middle" font-size="16" stroke="none" fill="{INK}">Osten</text></g>')
    return svg("".join(s), vb="0 0 600 880", uid=uid, cls="plan", top="".join(t))


# -------------------------------------------------- Lebendige Steine (Kirche aus Menschen)
def living_stones(uid="ls", words=None, blank=False):
    """Kirchensilhouette aus Steinen. words: Liste von Texten für die Steine."""
    import random
    rnd = random.Random(4)
    s = []
    rows = []
    # Hauptschiff 8 Reihen, Turm oben links
    y = 470
    rowh = 46
    for r in range(7):
        x = 70 + (r % 2) * 40
        while x < 470:
            w = rnd.choice([80, 90, 100])
            if x + w > 490:
                w = 490 - x
            if w > 30:
                rows.append((x, y - rowh, w, rowh))
            x += w
        y -= rowh
    # Dach (Dreieck) mit Steinen
    roof = f'<path d="M50 148 L270 30 L510 148Z" fill="{RED}" opacity=".85"/>'
    s.append(roof)
    s.append('<path d="M270 30 V0 M258 12 H282" stroke-width="4"/>')
    wi = 0
    for (x, yy, w, h) in rows:
        fill = rnd.choice([STONE, STONE2, "#e6dcc8", "#d2c2a4"])
        s.append(f'<rect x="{x+2}" y="{yy+2}" width="{w-4}" height="{h-4}" rx="8" fill="{fill}" stroke-width="2.6"/>')
        if words and not blank and wi < len(words):
            pass
    # Tür
    s.append(f'<path d="M240 470 V410 C240 384 300 384 300 410 V470Z" fill="#6b4d33"/>')
    t = []
    if words:
        # Wörter auf ausgewählte Steine verteilen (gut lesbar)
        pick = [i for i in range(len(rows)) if rows[i][2] >= 80 and not (230 < rows[i][0] + rows[i][2] / 2 < 310 and rows[i][1] > 380)]
        rnd.shuffle(pick)
        pick.sort(key=lambda i: -rows[i][2])
        words = sorted(words, key=len, reverse=True)
        for wtxt, idx in zip(words, pick):
            x, yy, w, h = rows[idx]
            if 230 < x + w / 2 < 310 and yy > 380:
                continue
            fs = min(15, (w - 10) * 1.75 / max(len(wtxt), 1))
            t.append(f'<text x="{x+w/2}" y="{yy+h/2+5}" text-anchor="middle" font-size="{fs:.1f}" stroke="none" fill="{INK}" font-weight="700">{wtxt}</text>')
    return svg("".join(s), vb="40 -6 480 482", uid=uid, cls="stones", top="".join(t))


# -------------------------------------------------------------- Embleme für Dienste
def emblem(key, uid="em"):
    """Kleine Sinnbilder für die Dienste in der Gemeinde (viewBox 200)."""
    E = {
        "pfarrer": f'''<path d="M70 30 C70 80 64 140 56 180 H84 C90 140 96 90 100 58 C104 90 110 140 116 180 H144 C136 140 130 80 130 30 C118 46 82 46 70 30Z" fill="{GREEN}"/>
            <path d="M72 150 H84 M116 150 H128 M78 160 V140 M122 160 V140" stroke="{GOLD}" stroke-width="3"/>''',
        "diakon": f'''<path d="M60 30 L140 170" stroke="{RED}" stroke-width="26"/><path d="M60 30 L140 170" stroke-width="2" opacity=".4"/>
            <path d="M96 92 L104 106 M92 102 L108 96" stroke="{GOLD}" stroke-width="3"/>''',
        "ministrant": f'''<path d="M60 40 H140 C140 64 120 76 100 76 C80 76 60 64 60 40Z" fill="#fffaf0"/>
            <path d="M68 70 L50 180 H150 L132 70" fill="#fffaf0"/><path d="M100 80 V180" stroke-width="2" opacity=".4"/>
            <path d="M58 40 H142" stroke="{RED}" stroke-width="8"/>''',
        "mesner": f'''<circle cx="74" cy="70" r="30" fill="{GOLD}"/><circle cx="74" cy="70" r="12" fill="{PAPER}"/>
            <path d="M98 88 L168 158 M140 130 L128 142 M156 146 L144 158" stroke-width="9"/><path d="M98 88 L168 158" stroke="{GOLD}" stroke-width="4"/>''',
        "organist": f'''<path d="M70 150 V60 L150 44 V134" fill="none" stroke-width="7"/><path d="M70 60 L150 44 V62 L70 78Z" fill="{INK}"/>
            <ellipse cx="56" cy="150" rx="20" ry="15" fill="{INK}"/><ellipse cx="136" cy="134" rx="20" ry="15" fill="{INK}"/>''',
        "lektor": g_lektionar(uid),
        "kommunionhelfer": g_hostienschale(uid),
        "pgr": f'''<ellipse cx="100" cy="118" rx="70" ry="26" fill="{LIGHTWOOD}"/>
            <path d="M40 60 C40 40 90 40 90 60 V78 H62 L50 90 V78 H40Z" fill="#fffaf0"/>
            <path d="M110 46 C110 28 164 28 164 46 V64 H152 V76 L140 64 H110Z" fill="#cfe1f2"/>
            <circle cx="50" cy="150" r="12" fill="{STONE}"/><circle cx="100" cy="158" r="12" fill="{STONE}"/><circle cx="150" cy="150" r="12" fill="{STONE}"/>''',
        "caritas": f'''<path d="M100 170 C40 126 22 96 30 70 C38 44 76 40 100 70 C124 40 162 44 170 70 C178 96 160 126 100 170Z" fill="{RED}"/>
            <path d="M74 98 H126 M100 72 V140" stroke="#fff" stroke-width="10"/>''',
        "chor": f'''<path d="M60 150 V50 L150 34 V134" fill="none" stroke-width="7"/>
            <ellipse cx="46" cy="150" rx="18" ry="13" fill="{INK}"/><ellipse cx="136" cy="134" rx="18" ry="13" fill="{INK}"/>
            <path d="M60 50 L150 34 V52 L60 68Z" fill="{INK}"/><path d="M150 34 C170 44 172 64 160 76" fill="none" stroke-width="3"/>''',
        "pastoral": f'''<circle cx="100" cy="70" r="28" fill="{STONE}"/><path d="M50 180 C50 120 150 120 150 180Z" fill="{BLUE}"/>
            <path d="M100 124 V176 M86 140 H114" stroke="#fff" stroke-width="6"/>''',
    }
    return svg(E[key], uid=uid + key, cls="emblem")


def ornament_line(w=600, uid="orn"):
    return svg(f'<path d="M10 20 C{w*0.25} 6 {w*0.4} 34 {w/2} 20 C{w*0.6} 6 {w*0.75} 34 {w-10} 20" fill="none" stroke-width="2.4"/>'
               f'<path d="M{w/2-8} 20 h16 M{w/2} 12 v16" stroke-width="2.4"/>', vb=f"0 0 {w} 40", uid=uid, cls="orn")
