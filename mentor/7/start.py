from secret import bot_name, key, link
import telebot
import time
print('Start telegram bot')
print(f'Bot name: {bot_name} KEY: {key}  Link:{link}')

bot = telebot.TeleBot(key)

questions = ['Как дела?', 'Что ты ел?', 'Молодец']

@bot.message_handler(commands=['start'])
def start_command(message):
    #print(message)
    username = message.from_user.username
    msg = f'Hello {username}'
    bot.send_message(message.chat.id,msg)
    bot.send_photo(message.chat.id, photo=open('girl.jpg', 'rb'))
    # for i in questions:
    #     time.sleep(3)
    #     bot.send_message(message.chat.id,i)

@bot.message_handler()
def get_message(message):
    print(message.text)

bot.polling()
