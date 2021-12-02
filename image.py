from PIL import Image
import ssl
import urllib.request

def update(url):
    ssl._create_default_https_context = ssl._create_unverified_context
    image = "sur.gif"

    r = urllib.request.urlopen(url)
    f = open(image, "wb")
    f.write(r.read())
    f.close()

    # From GIF palette to RGB formated PNG
    img = Image.open('sur.gif')
    cImg = img.convert('RGB')
    cImg.save("sur.png")

    # Crop borders, color scale, and time info
    img = Image.open('sur.png')
    cImg = img.crop((1, 55, 755, 734))
    cImg.save("sur.png")