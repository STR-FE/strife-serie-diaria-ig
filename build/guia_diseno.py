import json, os, subprocess, sys
from PIL import Image

BASE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(BASE)
MKT = os.path.expanduser('~/StudioProjects/strife-marketing')
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
TMP = os.path.join(BASE, 'diseno')

FONTS = os.path.join(BASE, "fonts") + "/"
CSS = """
@font-face { font-family:'Anton'; src:url('FONTS/anton.woff2') format('woff2'); }
@font-face { font-family:'JetBrains Mono'; font-weight:700; src:url('FONTS/jbmono-bold.woff2') format('woff2'); }
@font-face { font-family:'Inter'; src:url('FONTS/inter-regular.woff2') format('woff2'); }
* { margin:0; padding:0; box-sizing:border-box; }
html,body { width:1080px; height:1350px; overflow:hidden; }
body { position:relative; font-family:'Inter',sans-serif; color:#fff;
  background: radial-gradient(ellipse 900px 500px at 15% 100%, rgba(120,45,15,0.35), transparent 60%), #0b0c0e; }
.o { color:#e2571e; }
.label { font-family:'JetBrains Mono',monospace; font-weight:700; font-size:26px; letter-spacing:0.18em; color:#e2571e; }
.counter { font-family:'JetBrains Mono',monospace; font-weight:700; font-size:24px; letter-spacing:0.1em; color:#5f6064; }
.anton { font-family:'Anton',sans-serif; text-transform:uppercase; }
.sub { font-size:29px; line-height:1.35; color:#a2a2a3; }
.logo { position:absolute; font-family:'Anton',sans-serif; font-size:36px; }
.dev { position:absolute; overflow:hidden; background:#000; border:3px solid #26272b; }
.dev img { position:absolute; left:0; width:100%; }
.art { position:absolute; opacity:0.38; }
"""


def page(body, extra=''):
    css = CSS.replace('FONTS/', 'file://' + FONTS)
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{css}{extra}</style></head><body>{body}</body></html>'


def clamp(y, dev_h, sc, src_h=2400):
    return max(0, min(y, src_h - dev_h / sc))


def shot_url(cap):
    return 'file://' + os.path.join(MKT, cap + '.png')


def cover(v, g, s, i, n):
    l1, l2 = s['cover']
    fs = min(170 if v == 'B' else 150, int(940 / (0.46 * max(len(l1), len(l2)))))
    art = ''
    if v != 'A':
        art = f'<img class="art" src="file://{MKT}/reel/public/hares_transparent_bg.png" style="left:180px; top:820px; width:820px">'
    return page(f'''{art}
<div class="label" style="position:absolute;top:70px;left:72px">{g["label"]}</div>
<div class="counter" style="position:absolute;top:72px;right:72px">{i:02d} / {n:02d}</div>
<div class="anton" style="position:absolute;left:68px;top:{300 if v != 'A' else 470}px;font-size:{fs}px;line-height:0.92;white-space:nowrap">{l1}<br><span class="o">{l2}</span></div>
<div class="sub" style="position:absolute;left:72px;top:{300 + int(fs * 0.92 * 2) + 60 if v != 'A' else 820}px;width:{880 if v == 'A' else 620}px">{s["lead"]}</div>
<div class="label" style="position:absolute;left:72px;top:1180px;font-size:24px">{s.get("tag", "DESLIZA →")}</div>
<div class="logo" style="right:72px;bottom:60px">STR<span class="o">/</span>FE</div>''')


def step_A(g, s, i, n):
    sc = 434 / 1080
    y = clamp(s.get('a', 63), 940, sc)
    return page(f'''
<div class="label" style="position:absolute;top:70px;left:72px">{g["label"]}</div>
<div class="counter" style="position:absolute;top:72px;right:72px">{i:02d} / {n:02d}</div>
<div style="position:absolute;top:158px;left:68px;display:flex;align-items:flex-end;gap:14px">
  <div class="anton o" style="font-size:132px;line-height:0.78">{s["num"]}</div>
  <div class="anton" style="font-size:58px;line-height:0.95;padding-bottom:10px">{s["title"]}</div></div>
<div class="sub" style="position:absolute;top:300px;left:72px;width:940px">{s["sub"]}</div>
<div class="dev" style="left:320px;top:386px;width:440px;height:946px;border-radius:60px">
  <img src="{shot_url(s["cap"])}" style="top:{-y * sc:.0f}px"></div>
<div class="logo" style="left:72px;bottom:56px">STR<span class="o">/</span>FE</div>''')


def step_B(g, s, i, n):
    w = 980
    sc = w / 1080
    y = clamp(s.get('b', 63), 1100, sc)
    return page(f'''
<div style="position:absolute;top:58px;left:56px;right:56px;display:flex;justify-content:space-between">
  <div class="label">{g["label"]}</div><div class="counter">{i:02d} / {n:02d}</div></div>
<div style="position:absolute;top:118px;left:52px;display:flex;align-items:flex-end;gap:16px">
  <div class="anton o" style="font-size:120px;line-height:0.78">{s["num"]}</div>
  <div class="anton" style="font-size:62px;line-height:0.95;padding-bottom:6px">{s["title"]}</div></div>
<div class="sub" style="position:absolute;top:238px;left:56px;width:968px;font-size:28px">{s["sub"]}</div>
<div class="dev" style="left:50px;top:340px;width:{w}px;height:1100px;border-radius:64px 64px 0 0;border-bottom:0">
  <img src="{shot_url(s["cap"])}" style="top:{-y * sc:.0f}px"></div>
<div style="position:absolute;left:0;right:0;bottom:0;height:120px;background:linear-gradient(transparent,#0b0c0e)"></div>''')


def step_C(g, s, i, n):
    y = 63
    sc = 400 / 1080
    x0, y0, x1, y1 = s['focus']
    fw, fh = x1 - x0, y1 - y0
    zw = 560
    zs = zw / fw
    zh = fh * zs
    dev_left, dev_top = 600, 330
    fx = dev_left + 3 + x0 * sc
    fy = dev_top + 3 + (y0 - y) * sc
    ztop = max(560, min(1250 - zh, fy - zh / 2 + fh * sc / 2))
    return page(f'''
<div class="label" style="position:absolute;top:70px;left:72px">{g["label"]}</div>
<div class="counter" style="position:absolute;top:72px;right:72px">{i:02d} / {n:02d}</div>
<div style="position:absolute;top:150px;left:68px;display:flex;align-items:flex-end;gap:14px">
  <div class="anton o" style="font-size:120px;line-height:0.78">{s["num"]}</div>
  <div class="anton" style="font-size:56px;line-height:0.95;padding-bottom:8px">{s["title"]}</div></div>
<div class="sub" style="position:absolute;top:290px;left:72px;width:480px;font-size:28px">{s["sub"]}</div>
<div class="dev" style="left:{dev_left}px;top:{dev_top}px;width:406px;height:1100px;border-radius:52px 52px 0 0;border-bottom:0">
  <img src="{shot_url(s["cap"])}" style="top:{-y * sc:.0f}px"></div>
<div style="position:absolute;left:{fx - 6:.0f}px;top:{fy - 6:.0f}px;width:{fw * sc + 12:.0f}px;height:{fh * sc + 12:.0f}px;border:4px solid #e2571e;border-radius:14px"></div>
<svg style="position:absolute;left:0;top:0" width="1080" height="1350"><line x1="{40 + zw}" y1="{ztop + zh / 2:.0f}" x2="{fx - 6:.0f}" y2="{fy + fh * sc / 2:.0f}" stroke="#e2571e" stroke-width="4"/></svg>
<div style="position:absolute;left:40px;top:{ztop:.0f}px;width:{zw}px;height:{zh:.0f}px;border:5px solid #e2571e;border-radius:22px;overflow:hidden;background:#000;box-shadow:0 20px 60px rgba(0,0,0,.6)">
  <img src="{shot_url(s["cap"])}" style="position:absolute;width:{1080 * zs:.0f}px;left:{-x0 * zs:.0f}px;top:{-y0 * zs:.0f}px"></div>
<div class="logo" style="left:72px;bottom:56px">STR<span class="o">/</span>FE</div>''')


def render(html_path, out):
    cmd = [CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--force-device-scale-factor=1',
           '--allow-file-access-from-files', '--window-size=1080,1350', f'--screenshot={out}', 'file://' + html_path]
    for _ in range(3):
        try:
            subprocess.run(cmd, check=True, capture_output=True, timeout=60)
            return
        except subprocess.TimeoutExpired:
            subprocess.run(['pkill', '-f', html_path])
    raise SystemExit('Chrome no termina con ' + html_path)


def build(guia_json, variants):
    g = json.load(open(guia_json))
    n = len(g['slides'])
    for v in variants:
        d = os.path.join(TMP, g['id'], v)
        os.makedirs(d, exist_ok=True)
        for i, s in enumerate(g['slides'], 1):
            if 'cover' in s:
                html = cover(v, g, s, i, n)
            else:
                html = {'A': step_A, 'B': step_B, 'C': step_C}[v](g, s, i, n)
            hp = os.path.join(d, f'{i:02d}.html')
            open(hp, 'w').write(html)
            out = os.path.join(d, f'{i:02d}.png')
            render(hp, out)
            Image.open(out).convert('RGB').save(os.path.join(d, f'{i:02d}.jpg'), quality=90)
        print('ok', g['id'], v, n)


if __name__ == '__main__':
    build(sys.argv[1], sys.argv[2:] or ['A', 'B', 'C'])
