from PIL import Image
import scale, percentage

def scan():
    img = Image.open('sur.png')
    pixels = img.load()
    # (r, g, b) = pixels[x, y]

    imgW, imgH = img.size

    countLl = 0; countG = 0
    for i in range(imgW):
        for j in range(imgH):
            v = scale.compute(pixels[i, j])
            if v != -1:
                if v == 0:
                    countLl+=0.5
                elif v == 1:
                    countLl+=1
                elif v == 2:
                    countLl+=2
                elif v == 3:
                    countG+=1
                elif v == 4:
                    countG+=2

    if percentage.percentage(countLl) >= 20:
        #alerta lluvia
        print("Lluvias!")
    elif percentage.percentage(countG) >= 2.5:
        #alerta granizo!
        print("Granizo!!")
                
    print("Probabilidades de granizo (px):", countG, percentage.percentage(countG), "%")
    print("Probabilidades de lluvia (px): ", countLl , percentage.percentage(countLl), "%")
