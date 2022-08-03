import telebot
import config

bot = telebot.TeleBot(config.Token)

@bot.message_handler(commands=['start'])
def welcome(message):
    with open('welcome.webp', 'rb') as file: 
        sticker = file.read()

    bot.send_sticker(chat_id=message.chat.id, sticker=sticker)
    bot.send_message(chat_id=message.chat.id, text='Welcome!')

@bot.message_handler(commands=['address'])
def print_address(message):
    bot.send_location(chat_id=message.chat.id, latitude=48.51, longitude=2.17, )
    with open('Когда идёт дождь.mp3', 'rb') as file: 
        audio = file.read()
    with open('welcome.webp', 'rb') as file: 
        sticker = file.read()