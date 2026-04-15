"""Generate OG image (1200x630 PNG) for SA-Flow social sharing."""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1200, 630

img = Image.new("RGB", (W, H), "#0145F2")
draw = ImageDraw.Draw(img)

# Gradient background (top to bottom: #0145F2 → #0033BB)
for y in range(H):
    r = int(1 + (0 - 1) * y / H)
    g = int(69 + (51 - 69) * y / H)
    b = int(242 + (187 - 242) * y / H)
    draw.line([(0, y), (W, y)], fill=(r, g, b))

# Decorative circles (subtle)
draw.ellipse((-120, -120, 280, 280), fill=(20, 80, 255))
draw.ellipse((900, 400, 1400, 900), fill=(0, 45, 200))

# Gold accent line
draw.rectangle([(80, 280), (200, 284)], fill="#F7B538")

# Try to load a nice font, fall back to default
try:
    font_big = ImageFont.truetype("arial.ttf", 72)
    font_med = ImageFont.truetype("arial.ttf", 32)
    font_sm = ImageFont.truetype("arial.ttf", 22)
except:
    font_big = ImageFont.load_default()
    font_med = ImageFont.load_default()
    font_sm = ImageFont.load_default()

# "SA-Flow" logo text
draw.text((80, 80), "⚡ SA-Flow", fill="white", font=font_big)

# Tagline
draw.text((80, 200), "Professional Websites", fill="white", font=font_med)
draw.text((80, 240), "for Every Business", fill=(200, 210, 255), font=font_med)

# Bottom info
draw.text((80, 340), "38+ Business Categories  |  Starting at Rs.1,500", fill=(200, 210, 255), font=font_sm)
draw.text((80, 380), "Based in Ranchi, India  |  saflow.app", fill=(170, 185, 240), font=font_sm)

# Pricing badges
badge_y = 460
badges = [("Basic", "₹1,500"), ("Medium", "₹2,500"), ("Advanced", "₹5,000")]
x_pos = 80
for name, price in badges:
    # Badge background
    bw = 200
    draw.rounded_rectangle((x_pos, badge_y, x_pos + bw, badge_y + 80), radius=12, fill=(30, 60, 200))
    draw.text((x_pos + 20, badge_y + 12), name, fill=(200, 210, 255), font=font_sm)
    draw.text((x_pos + 20, badge_y + 42), price, fill="white", font=font_med)
    x_pos += bw + 24

# "saflow.app" bottom-right
draw.text((W - 250, H - 50), "saflow.app", fill=(150, 170, 230), font=font_sm)

out = os.path.join(os.path.dirname(__file__), "og-image.png")
img.save(out, "PNG", quality=95)
print(f"✅ OG image saved: {out} ({W}x{H})")
