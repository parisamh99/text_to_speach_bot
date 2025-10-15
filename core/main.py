import telebot
import os 
import logging
from gtts import gTTS

API_TOKEN = os.environ.get("API_TOKEN")

bot = telebot.TeleBot(API_TOKEN)    

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.send_message(message.chat.id,"send me a text and i will read it for you")

@bot.message_handler(func=lambda message:True)
def text_to_speach(message):
    text = message.text
    file_path = "voices/output.mp3"
    audio = gTTS(text=text ,lang="en",tld='com.au')
    audio.save(file_path)
    bot.send_voice(chat_id=message.chat.id,reply_to_message_id=message.id,voice=open(file_path,"rb"))
    os.remove(file_path)

bot.infinity_polling()