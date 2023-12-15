import telebot
from io import BytesIO
from gtts import gTTS
TOKEN = '6718634779:AAGISQ4HkrV3NZY0XxLYz5cnXG53zxpCDJU'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['audio'])
def audio(message):
    audio_resourse = open('Wham-Last_Christmas.mp3', 'rb')
    bot.send_audio(message.chat.id, audio_resourse)
@bot.message_handler(content_types=['voice'])
def voice_from_user(message):
    photo_to_send = open('voice.jpg', 'rb')
    bot.send_photo(message.chat.id, photo_to_send)
def converter(text: str) -> BytesIO:
    bytes_file = BytesIO()
    new_audio = gTTS(text=text, lang="ru")
    new_audio.write_to_fp(bytes_file)
    bytes_file.seek(0)
    return bytes_file
@bot.message_handler(content_types=['text'])
def text_from_user(message):
    voice = converter(message.text)
    bot.send_voice(message.chat.id, voice)
@bot.message_handler(commands=['photo'])
def photo(message):
    photo_to_send = open('cat.jpg', 'rb')
    bot.send_photo(message.chat.id, photo_to_send)
    bot.send_message(message.chat.id, 'Котик')
bot.polling(none_stop=True)