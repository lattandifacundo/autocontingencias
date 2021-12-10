from PIL import Image
import scale, percentage

def scan(imagePath):
    img = Image.open(imagePath)
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

    print("Probabilidades de granizo (px):", countG, percentage.percentage(countG), "%")
    print("Probabilidades de lluvia (px): ", countLl , percentage.percentage(countLl), "%")

    Llpercentage = percentage.percentage(countLl)
    Gpercentage = percentage.percentage(countG)
    if Gpercentage >= 2.5:
        print("Granizo!, Sending report")
        import telegram
        telegram.sendPost(
            text="<b>⛈ Granizará</b>\n<code>"+str(Gpercentage)+"%</code>",
            imagesPaths=['docs/src/granizo.png', 'sur.png'],
            needNotification=True
        )
    elif Llpercentage >= 20:
        print("Lluvias!, Sending report")
        import telegram
        telegram.sendPost(
            text="<b>🌧 Lloverá</b>\n<code>"+str(Llpercentage)+"%</code>",
            imagesPaths=['docs/src/lluvia.png', 'sur.png'],
            needNotification=False
        )
    else:
        print("✔ No report needed")
