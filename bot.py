import telebot

bot = telebot.TeleBot("638320583:AAGsE7HjfM6cFfIVXv6WvVg8LWhoIwv9pC8")


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text == 'Пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')
    elif message.text == 'Я Оксана':
        bot.send_message(message.chat.id, 'О, госпожа Николаева! Как там Доник?')


bot.polling()
