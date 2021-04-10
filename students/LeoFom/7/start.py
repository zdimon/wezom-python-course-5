from secret import bot_name, key, link
import telebot
import time

print(f'Bot name: {bot_name}, Key: {key}, Link: {link} .')

bot = telebot.TeleBot(key)

import random

@bot.message_handler(commands=['start'])
def start_command(message):
    print('Got message')
    username = message.from_user.username
    for i in range(5):
        time.sleep(3)
        L=['Hi!','How are you? ','Where are you from?','How old are you? ','You are good']
        msg = f'{L[i]} {username}'
        bot.send_message(message.chat.id,msg)

@bot.message_handler()
def get_message(message):
    if message.text=='Hi':
        msg= 'Oh, hi, how are you?'
        bot.send_message(message.chat.id,msg)
    if message.text=='Пляж':
        time.sleep(3)
        bot.send_message(message.chat.id,"Я не пляж. Сам ты пляж!!!")
    print(message.text)
    bot.send_photo(message.chat.id, photo=open('dog.jpg','rb'))

bot.polling()