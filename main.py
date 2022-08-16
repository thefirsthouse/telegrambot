import telebot

bot = telebot.TeleBot('5423927067:AAEQssnN9znOVw2Kng2T_I8TJmL5pF-JfpE')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Здравствуйте, {message.from_user.first.name}')



bot.polling(none_stop=True)