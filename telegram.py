import telebot, os, decouple
from telebot.types import InputMediaAnimation, InputMediaPhoto, InputMediaVideo

TOKEN = decouple.config('TOKEN')
CHANNEL_ID = decouple.config('CHANNEL_ID')
PHOTO_URL = decouple.config('RADAR_URL')

bot = telebot.TeleBot(TOKEN)

def sendPost(text, imagesPaths, needNotification):
    images = []
    for x in imagesPaths:
        if x == imagesPaths[0]:
            images.append(InputMediaPhoto(open(x, 'rb'), caption=text, parse_mode="HTML"))
        else:
            if x == 'animacion.mp4':
                images.append(InputMediaVideo(open(x, 'rb')))
            else:
                images.append(InputMediaPhoto(open(x, 'rb')))

    bot.send_media_group(CHANNEL_ID, images, disable_notification= not needNotification)
