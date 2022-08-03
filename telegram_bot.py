import telebot
#import config
bot = telebot.TeleBot("5327841709:AAH5PbpyNc52GYTwEFSY6s8Se77trqbaygs")

@bot.message_handler(commands=['start'])
def start_message(message):
    #with open('welcome.webp', 'rb') as file: 
     #   sticker = file.read()

   # bot.send_sticker(chat_id=message.chat.id, sticker=sticker)
    bot.send_message(message.chat.id, "Привет")
    bot.infinity_polling()