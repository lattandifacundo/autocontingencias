from PIL import Image
import scale

def scan():
    img = Image.open('sur.png')
    pixels = img.load()
    # (r, g, b) = pixels[x, y]

    imgW, imgH = img.size

    countLl = 0; countG = 0
    for i in range(imgW):
        for j in range(imgH):
            v = scale.compute(pixels[i, j])
            if v == 1:
                countLl+=1
            elif v == 2:
                countG+=2
                
    print("Probabilidades de granizo (px):", countG, "\nProbabilidades de lluvia (px): ", countLl)
