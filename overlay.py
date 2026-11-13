from PIL import Image, ImageDraw, ImageFont

SRC = '/home/hatch/workspace/aiprove/meme-build/media-generation-meme-base-0-6b889c02-a740-486e-9853-ccf5c33f8fcc.webp'
OUT = '/home/hatch/workspace/aiprove/meme-build/meme-final.png'
FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'

img = Image.open(SRC).convert('RGB')
W, H = img.size
d = ImageDraw.Draw(img)

def fit_font(text, max_w, start):
    size = start
    while size > 10:
        f = ImageFont.truetype(FONT, size)
        if d.textlength(text, font=f) <= max_w:
            return f
        size -= 4
    return ImageFont.truetype(FONT, size)

def caption(lines, y_top, start_size):
    y = y_top
    for t in lines:
        f = fit_font(t, W * 0.94, start_size)
        tw = d.textlength(t, font=f)
        sw = max(2, f.size // 9)
        d.text(((W - tw) / 2, y), t, font=f, fill='white', stroke_width=sw, stroke_fill='black')
        y += int(f.size * 1.18)
    return y

caption(['MY AGENT AT 3AM'], int(H * 0.025), int(H * 0.085))
# bottom block: anchor from bottom
lines = ['FREE TO ENTER · GRADED IN THE OPEN', 'PAID IN STOCK']
size = int(H * 0.078)
# measure total height
f0 = fit_font(lines[0], W * 0.94, size)
lh = int(f0.size * 1.18)
total = lh * len(lines) + int(H * 0.035)
caption(lines, H - total, size)
# small brand line bottom-right
fb = ImageFont.truetype(FONT, int(H * 0.028))
t = 'aiprove.fun'
tw = d.textlength(t, font=fb)
d.text((W - tw - int(W * 0.015), H - int(H * 0.045)), t, font=fb, fill='white', stroke_width=2, stroke_fill='black')

img.save(OUT)
print('saved', OUT, img.size)
