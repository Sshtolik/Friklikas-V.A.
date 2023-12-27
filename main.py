import telebot

TOKEN = '6711340991:AAGLFGIo_-4dprRPA0wz_bnJ1agcLyXXGnI'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands = ['sticker'])
def send_sticker(message):
    hi_sticker = open('hi.png', 'rb')
    bot.send_sticker(message.chat.id, hi_sticker)
    bot.send_message(message.chat.id, 'Привет! &#128516;', parse_mode='HTML')

bot.polling(none_stop=True)