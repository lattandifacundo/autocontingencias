from PIL import Image
import ssl, urllib.request, os

cachedSecret = ""

def update(url):
    global cachedSecret; cachedSecret = url

    try:
        ssl._create_default_https_context = ssl._create_unverified_context
        image = "sur.gif"

        r = urllib.request.urlopen(url+image)
        f = open(image, "wb")
        f.write(r.read())
        f.close()
    except:
        print("❌ Error al descargar la imagen")
        exit(0)

    # From GIF palette to RGB formated PNG
    img = Image.open('sur.gif')
    cImg = img.convert('RGB')
    cImg.save("sur.png")

    # Crop borders, color scale, and time info
    img = Image.open('sur.png')
    cImg = img.crop((1, 55, 755, 734))
    cImg.save("sur.png")

def downloadAdditions():
    try:
        ssl._create_default_https_context = ssl._create_unverified_context
        image = "animacion.gif"

        r = urllib.request.urlopen(cachedSecret+image)
        f = open(image, "wb")
        f.write(r.read())
        f.close()

        #Gif to Mp4
        import moviepy.editor as mp

        clip = mp.VideoFileClip("animacion.gif")
        clip.to_RGB()
        clip.write_videofile("animacion.mp4")
    except:
        print("❌ Error al descargar las adiciones")
        exit(0)