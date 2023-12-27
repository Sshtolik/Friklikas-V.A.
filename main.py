import telebot
from telebot import types
from geopy.geocoders import Nominatim

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
@bot.message_handler(commands=['place'])
def place(message):
    bot.send_message(message.chat.id, 'Нашёл для тебя интересное место:')
    bot.send_location(message.chat.id, 55.760382, 37.618255)
@bot.message_handler(commands=['place1'])
def place1(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    button_geo = types.KeyboardButton(text='Разрешить доступ к геолокации',
                                      request_location=True)
    keyboard.add(button_geo)
    bot.send_message(message.chat.id,
                     'Я умею работать с геолокацией! \nНо для начала мне нужно твое разрешение',
                     reply_markup=keyboard)
@bot.message_handler(content_types=['location'])
def location_from_user(message):
    bot.send_message(message.chat.id, 'Отличное место! Обязательно добавлю его в свой список')
@bot.message_handler(commands=['place2'])
def place(message):
    geolocation = Nomination(user_agent="GetLoc")
    location_name = geolocation.reverse('55.760382, 37.618255')
    bot.send_message(message.chat.id,
                     f'Выбранное место расположено по адресу: \n{location_name.address}')
bot.polling(none_stop=True)