from PIL import Image
import scale, percentage

def scan(imagePath):
    img = Image.open(imagePath)
    pixels = img.load()
    # (r, g, b) = pixels[x, y]

    imgW, imgH = img.size

    countG = 0 # Count "granizo" pixels
    for i in range(imgW):
        for j in range(imgH):
            v = scale.compute(pixels[i, j])
            if v != -1:
                if v == 3 or v == 4:
                    countG+=1

    percentageG = percentage.percentage(countG)
    print("⛈ Granizo detectado:\n\t" + str(countG) + "px\n\t" + str(percentageG) + "%")
    
    if percentageG >= 4:
        print("🔴 Red alert!, Sending report")
        import telegram, message, update
        update.downloadAdditions()
        telegram.sendPost(
            text=message.template('red'),
            imagesPaths=['docs/src/redAlert.webp', 'sur.gif', 'animacion.mp4'],
            needNotification=True
        )
    elif percentageG >= 3:
        print("🟡 Yellow alert!, Sending report")
        import telegram, message, update
        update.downloadAdditions()
        telegram.sendPost(
            text=message.template('yellow'),
            imagesPaths=['docs/src/yellowAlert.webp', 'sur.gif', 'animacion.mp4'],
            needNotification=True
        )
    elif percentageG >= 2.5:
        print("🟢 Green alert!, Sending report")
        import telegram, message, update
        update.downloadAdditions()
        telegram.sendPost(
            text=message.template('green'),
            imagesPaths=['docs/src/greenAlert.webp', 'sur.gif', 'animacion.mp4'],
            needNotification=False
        )
    else:
        print("✔ No report needed")
