import telebot
import os
from credentials import *
import speech_recognition as sr

from aux.play_radio.radio import *

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    chat_id = message.chat.id

    if chat_id == 166202574:
        bot.reply_to(message,'Hey')
    else:
        bot.reply_to(message,"Sorry, I can't help you")

@bot.message_handler(content_types=['voice'])
def handle_docs_audio(message):
    try:
        chat_id = message.chat.id

        if chat_id == CHAT_ID:
            file_id = message.voice.file_id
            file_info = bot.get_file(file_id)
            downloaded_file = bot.download_file(file_info.file_path)

            voice_id = str(chat_id) + ".ogg"
            with open(voice_id, 'wb') as new_file:
                new_file.write(downloaded_file)

            os.system('ffmpeg -i '+ voice_id + ' -y ' + str(chat_id) + '.wav -loglevel panic') 
            r = sr.Recognizer()
            harvard = sr.AudioFile(str(chat_id)+'.wav')

            with harvard as source:
                audio = r.record(source)

            recognized_string = r.recognize_google(audio,language=LANGUAGE)

            if recognized_string == 'random radio':
                play_random_radio()
            elif recognized_string == 'stop radio':
                stop_radio()
            elif 'play radio' in recognized_string:
                play_radio(recognized_string.split()[-1])
            elif recognized_string == 'list radios':
                bot.reply_to(message, list_radios())
            else:
                bot.reply_to(message, 'Hmmm, what is "' + recognized_string + '?"')
        else:
            bot.reply_to(message, 'no')

    except Exception as e:
        bot.reply_to(message, e)
        log.error(e)

while True:
    try:
        bot.infinity_polling(True)
    except Exception as e:
        time.sleep(15)
        log.error(e)
