import telebot

TOKEN = '6711340991:AAGLFGIo_-4dprRPA0wz_bnJ1agcLyXXGnI'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands = ['sticker'])
def send_sticker(message):
    hi_sticker = open('hi.png', 'rb')
    bot.send_sticker(message.chat.id, hi_sticker)
    bot.send_message(message.chat.id, 'Привет! &#128516;', parse_mode='HTML')
@bot.message_handler(content_types=['sticker'])
def sticker_from_user(message):
    sticker_id = message.sticker.file_id
    bot.send_message(message.chat.id, f'Отличный стикер! &#128513; '
                                      f'\nВот его id: \n<b>{sticker_id}</b>'
                                      f'\nТеперь я могу использовать его &#128522;',
                     parse_mode='HTML')
    bot.send_sticker(message.chat.id, sticker_id)

bot.polling(none_stop=True)