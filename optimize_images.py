from PIL import Image
import os

for name in ['bloomnest', 'saerp', 'parkmanager']:
    img = Image.open(f'screenshots/{name}.png')
    img.save(f'screenshots/{name}.webp', 'WEBP', quality=82, method=6)
    img.save(f'screenshots/{name}.png', 'PNG', optimize=True)
    png_size = os.path.getsize(f'screenshots/{name}.png')
    webp_size = os.path.getsize(f'screenshots/{name}.webp')
    print(f'{name}: PNG={png_size//1024}KB  WebP={webp_size//1024}KB  ({100-webp_size*100//png_size}% smaller)')

img = Image.open('og-image.png')
img.save('og-image.webp', 'WEBP', quality=85, method=6)
og_png = os.path.getsize('og-image.png')
og_webp = os.path.getsize('og-image.webp')
print(f'og-image: PNG={og_png//1024}KB  WebP={og_webp//1024}KB')
