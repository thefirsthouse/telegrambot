import telebot
from telebot import types

# import bot system

bot = telebot.TeleBot('5668164800:AAEvffIHxrjKRsBpa6L6yW8MegaME55ifoo')


# bot token

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
                     f'сап. этот бот поможет тебе купить бит или сделать заказ.\nвыбери то, что тебе нужно в меню.',
                     reply_markup=markup)


# tracking "start" command

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton('биты 🎹')
item2 = types.KeyboardButton('сведение 🎧')
item3 = types.KeyboardButton('прочие услуги 🎤')
markup.add(item1, item2, item3)


# adding buttons

@bot.message_handler(content_types=['text'])
def service(message):
    if message.chat.type == 'private':
        if message.text == 'биты 🎹':
            bot.send_message(message.chat.id, 'выбери номер в каталоге, и отправь его',
                             reply_markup=markup2)
            if message.chat.type == 'private':
                if message.text == 'cheese - 1':
                    bot.send_message(message.chat.id,'проверь бит, если всё правильно - жми да\n\nhttps://t.me/blueberrybeats/11')
        if message.text == 'сведение 🎧':
            bot.send_message(message.chat.id,
                             'отправь архив в формате <b>rar</b> или <b>zip</b>\nв архиве должны быть:\n1. wav('
                             'желательно) файлы с <b>трек аутом</b> бита(если нет трек аута, просто wav файл с '
                             'битом)\n2. чистые wav файлы с <b>вокалом</b>(основным <b>вокалом</b>, <b>даблами</b>('
                             'если есть), <b>бэками</b> и <b>эдлибами</b>\n3. прочие wav дорожки(<b>sfx</b> и '
                             'т.д.)\n\nесли архив соответсвует стандарту - смело отправляй',
                             parse_mode='html')
        if message.text == 'прочие услуги 🎤':
            bot.send_message(message.chat.id, 'выбери услугу', reply_markup=markup1)

@bot.message_handler(content_types=['text'])
def catalog(message):
    if message.chat.type == 'private':
        if message.text == 'cheese - 1':
            bot.send_message(message.chat.id, 'проверь бит, если всё правильно - жми да\n\nhttps://t.me/blueberrybeats/11')

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'gavno')


markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
item4 = types.KeyboardButton('заказ уникального бита')
item5 = types.KeyboardButton('трек под ключ')
markup1.add(item4, item5)
# adding buttons

markup2 = markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
beat1 = types.KeyboardButton('cheese - 1')
beat2 = types.KeyboardButton('')
markup2.add(beat1, beat2)


bot.polling(none_stop=True)
