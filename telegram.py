import telebot, os, decouple
from telebot.types import InputMediaPhoto

TOKEN = decouple.config('TOKEN')
CHANNEL_ID = decouple.config('CHANNEL_ID')
PHOTO_URL = decouple.config('RADAR_URL')

bot = telebot.TeleBot(TOKEN)

def sendPost(text, imagesPaths, needNotification):
    images = []
    try:
        for x in imagesPaths:
            if x == imagesPaths[0]:
                images.append(InputMediaPhoto(open(x, 'rb'), caption=text, parse_mode="HTML"))
            else:
                images.append(InputMediaPhoto(open(x, 'rb')))
    except x:
        print("❌ Ha ocurrido un error al leer las imagenes"+ str(x) +"\nfrom telegram.py")
        exit(1)

    try:
        bot.send_media_group(CHANNEL_ID, images, disable_notification= not needNotification)
    except:
        print("❌ Ha ocurrido un error al enviar el mensaje+\nfrom telegram.py")
        exit(1)
