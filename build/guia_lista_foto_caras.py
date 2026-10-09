# guia-lista-foto: las caras de la foto de grupo son reales. Sustituye las de los renders de
# guia_diseno.py por las caras alteradas del resumen (mod/08 mod.jpeg), para que cada alumno tenga la
# misma cara en todas las fotos. La 04 se usa tal cual (mod/04 mod.jpeg, caras diminutas).
#   python3 guia_diseno.py ../../strife-marketing/serie-v2/guias/lista-foto.json B && python3 guia_lista_foto_caras.py
from PIL import Image, ImageDraw, ImageFilter

REPO = '/Users/jaimevillalba/StudioProjects/strife-serie-diaria-ig'
B = REPO + '/build/diseno/guia-lista-foto/B'
MOD = B + '/../mod/08 mod.jpeg'
OUT = REPO + '/jpg/guia-lista-foto'

def tiles():
    m = Image.open(MOD).convert('RGB')
    xs = [(88, 178), (226, 316), (364, 454), (502, 592), (640, 730)]
    ys = [(430, 518), (614, 702), (798, 888)]
    out = []
    for r, (y0, y1) in enumerate(ys):
        for c, (x0, x1) in enumerate(xs):
            if r == 2 and c > 2:
                break
            out.append(m.crop((x0 + 7, y0 + 7, x1 - 7, y1 - 7)))
    return out  # cara 1..13

def circle(img, face, cx, cy, r, clip_x=None):
    d = 2 * r
    f = face.resize((d, d), Image.LANCZOS)
    mask = Image.new('L', (d * 4, d * 4), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, d * 4 - 1, d * 4 - 1), fill=255)
    mask = mask.resize((d, d), Image.LANCZOS)
    if clip_x and cx + r > clip_x:
        cut = clip_x - (cx - r)
        f, mask = f.crop((0, 0, cut, d)), mask.crop((0, 0, cut, d))
    img.paste(f, (cx - r, cy - r), mask)

def strip(img, T, dy=0):
    # miniatura de la cara actual (cara 2) y tira de caras 1..10
    circle(img, T[1], 145, 415 + dy, 47)
    for k in range(10):
        cx = 131 + 97 * k
        r = 34
        circle(img, T[k], cx, 533 + dy, r, clip_x=1026)
    return img

def boxed(img, face, box, radius, inset, zoom=1.25):
    # la cara ampliada dentro de su recuadro: el centro de la ficha, sin el margen de 1,7x
    x0, y0, x1, y1 = box
    w, h = face.size
    cw, ch = w / zoom, h / zoom
    f = face.crop(((w - cw) / 2, (h - ch) / 2 - h * 0.03, (w + cw) / 2, (h + ch) / 2 - h * 0.03))
    bw, bh = x1 - x0 - 2 * inset, y1 - y0 - 2 * inset
    f = f.resize((bw, bh), Image.LANCZOS).filter(ImageFilter.UnsharpMask(2, 60, 2))
    mask = Image.new('L', (bw * 4, bh * 4), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, bw * 4 - 1, bh * 4 - 1), radius=radius * 4, fill=255)
    mask = mask.resize((bw, bh), Image.LANCZOS)
    if x0 + inset + bw > 1026:
        cut = 1026 - (x0 + inset)
        f, mask = f.crop((0, 0, cut, bh)), mask.crop((0, 0, cut, bh))
    img.paste(f, (x0 + inset, y0 + inset), mask)

def grid(img, T):
    # resumen: 5 columnas, 13 fichas
    for k, face in enumerate(T):
        x0, y0 = 114 + round(182.5 * (k % 5)), 564 + 244 * (k // 5)
        boxed(img, face, (x0, y0, x0 + 122, y0 + 122), 18, 5, zoom=1)


def build(n, out):
    T = tiles()
    img = Image.open(f'{B}/{n}.jpg').convert('RGB')
    if n == '08':
        grid(img, T)
    if n == '06':
        strip(img, T)
    if n == '05':
        strip(img, T, dy=527)
        boxed(img, T[1], (455, 470, 627, 641), 30, 5)
        boxed(img, T[3], (673, 425, 851, 602), 34, 7)
        boxed(img, T[4], (940, 405, 1118, 582), 34, 7)
    img.save(out, quality=92)


if __name__ == '__main__':
    for n in ('05', '06', '08'):
        build(n, f'{OUT}/{n}.jpg')
    Image.open(B + '/../mod/04 mod.jpeg').convert('RGB').resize((1080, 1350), Image.LANCZOS).save(f'{OUT}/04.jpg', quality=92)
    print('ok 04 05 06 08')
