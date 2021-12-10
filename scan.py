from PIL import Image
import scale, percentage

def scan(imagePath):
    img = Image.open(imagePath)
    pixels = img.load()
    # (r, g, b) = pixels[x, y]

    imgW, imgH = img.size

    countG = 0
    for i in range(imgW):
        for j in range(imgH):
            v = scale.compute(pixels[i, j])
            if v != -1:
                if v == 3 or v == 4:
                    countG+=1

    percentageG = percentage.percentage(countG)
    print("⛈ Granizo detectado:\n\t" + str(countG) + "px\n\t" + str(percentageG) + "%")
    
    if percentageG >= 3:
        print("🔴 Red alert!, Sending report")
        import telegram
        telegram.sendPost(
            text="⛈ Se ha detectado <b>granizo</b> en las nubes\n<code>"+str(countG) + "px\n" + str(percentageG) + "%</code>",
            imagesPaths=['sur.png'],
            # imagesPaths=['docs/src/redGranizo.png', 'sur.png'],
            needNotification=True
        )
    elif percentageG >= 2:
        print("🟡 Yellow alert!, Sending report")
        import telegram
        telegram.sendPost(
            text="⛈ Se ha detectado <b>granizo</b> en las nubes\n<code>"+str(countG) + "px\n" + str(percentageG) + "%</code>",
            imagesPaths=['sur.png'],
            # imagesPaths=['docs/src/yellowGranizo.png', 'sur.png'],
            needNotification=True
        )
    else:
        print("✔ No report needed")
