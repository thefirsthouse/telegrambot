import telebot
## import bot system

bot = telebot.TeleBot('5668164800:AAEvffIHxrjKRsBpa6L6yW8MegaME55ifoo')
## bot token

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'сап. этот бот поможет тебе купить бит или сделать заказ.\nвыбери то, что тебе нужно в меню.', reply_markup=markup)
## tracking "start" command

from telebot import types
## import buttons system

markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
item1 = types.KeyboardButton('биты 🎹')
item2 = types.KeyboardButton('сведение 🎧')
item3 = types.KeyboardButton('прочие услуги 🎤')
markup.add(item1, item2, item3)
## adding buttons

import io

@bot.message_handler(content_types=['text'])
def service(message):
    if message.chat.type == 'private':
        if message.text == 'биты 🎹':
            bot.send_message(message.chat.id, 'выберите номер в каталоге, и отправьте его')
            @bot.message_handler(content_types=['text'])
            def catalog(message):
                if message.chat.type == 'private':
                    if message.text == '1':
                        beat = open('beats/govno.mp3', 'rb')
                        bot.send_audio(message.chat.id, beat, 'гавно')

bot.polling(none_stop=True)