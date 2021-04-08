# Подключаем модуль secret
from secret import bot_name, key, link
# Подключаем модуль для Телеграма
import telebot
import time
# Указываем токен
bot = telebot.TeleBot(key)
# Импортируем типы из модуля, чтобы создавать кнопки
from telebot import types

print('Start telegram bot')
print(f'Bot name: {bot_name} KEY: {key}  Link:{link}')

# Метод, который получает сообщения и обрабатывает их
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # Если написали «Привет»
    if message.text.lower() == "привет":
        # Пишем приветствие
        username = message.from_user.username
        bot.send_message(message.from_user.id, f"Привет {username}, сейчас я покажу какими клавишами можно войти в BIOS.")
        # Готовим кнопки
        keyboard = types.InlineKeyboardMarkup()
        # По очереди готовим текст и обработчик для каждой кнопки
        key_del = types.InlineKeyboardButton(text='Del', callback_data='keydel')
        # И добавляем кнопку на экран
        keyboard.add(key_del)
        key_esc = types.InlineKeyboardButton(text='Esc', callback_data='keyesc')
        keyboard.add(key_esc)            
        key_f1 = types.InlineKeyboardButton(text='F1', callback_data='keyf1')
        keyboard.add(key_f1)
        key_f2 = types.InlineKeyboardButton(text='F2', callback_data='keyf2')
        keyboard.add(key_f2)
        key_f3 = types.InlineKeyboardButton(text='F3', callback_data='keyf3')
        keyboard.add(key_f3)
        key_f8 = types.InlineKeyboardButton(text='F8', callback_data='keyf8')
        keyboard.add(key_f8)
        key_f10 = types.InlineKeyboardButton(text='F10', callback_data='keyf10')
        keyboard.add(key_f10)
        key_f12 = types.InlineKeyboardButton(text='F12', callback_data='keyf12')
        keyboard.add(key_f12)
        key_CtrlF2 = types.InlineKeyboardButton(text='Ctrl+F2', callback_data='keyCtrlF2')
        keyboard.add(key_CtrlF2)
        key_CtrlAltEsc = types.InlineKeyboardButton(text='Ctrl+Alt+Esc', callback_data='keyCtrlAltEsc')
        keyboard.add(key_CtrlAltEsc)
        key_CtrlAltS = types.InlineKeyboardButton(text='Ctrl+Alt+S', callback_data='keyCtrlAltS')
        keyboard.add(key_CtrlAltS)        
        key_CtrlAltEnter = types.InlineKeyboardButton(text='Ctrl+Alt+Enter', callback_data='key_CtrlAltEnter')
        keyboard.add(key_CtrlAltEnter)
       
        # Показываем все кнопки сразу и пишем сообщение о выборе
        bot.send_message(message.from_user.id, text='Выбери клавишу', reply_markup=keyboard)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши Привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    # Если нажали на одну из кнопок — выводим информацию
    if call.data == "keydel": 
        # Формируем ответ
        msg = "Acer (Aspire, Power, Veriton, Extensa, Ferrari, TravelMate, Altos), ASRock, ABIT, ASUS, AMI (American Megatrends AMIBIOS, AMI BIOS), Award BIOS (AwardBIOS), Compaq (Older Computers), Chaintech, Dell Dimension L566cx System, "
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)
    if call.data == "keyesc":
        msg = "Большинство моделей Toshiba, Cybermax, "
        bot.send_message(call.message.chat.id, msg)
    if call.data == "keyf1":
        msg = "Все модификации IBМ, Lenovo, некоторые HP, Dell, Packard-Bell, Gateway, Acer (Aspire, Power, Veriton, Extensa, Ferrari, TravelMate, Altos, Older PC), AMI (American Megatrends AMIBIOS, AMI BIOS) – Old Version, BIOSTAR, Compaq (Older Computers), "
        bot.send_message(call.message.chat.id, msg)
    if call.data == "keyf2":
        msg = "Acer, ASRock, Asus, RoverBook, AMI (American Megatrends AMIBIOS, AMI BIOS) – Old Version, Compaq (Older Computers), Dell (XPS, Dimension, Inspiron, Latitude. OptiPlex, Precision, Vostro), "
        bot.send_message(call.message.chat.id, msg)    
    if call.data == "keyf3":
        msg = "Редко встречается у Dell, Sony"
        bot.send_message(call.message.chat.id, msg)
    if call.data == "keyf8":
        msg = "iRu, некоторые модификации Dell"
        bot.send_message(call.message.chat.id, msg)
    if call.data == "keyf10":
        msg = "Toshiba, Compaq (Presario, Prolinea, Deskpro, Systempro, Portable), Compaq (Older Computers), "
        bot.send_message(call.message.chat.id, msg)
    if call.data == "keyf12":
        msg = "Некоторые модели Lenovo"
        bot.send_message(call.message.chat.id, msg)
    if call.data == "keyCtrlF2":
        msg = "Asus"
        bot.send_message(call.message.chat.id, msg)
    if call.data == "keyCtrlAltEsc":
        msg = "Acer (Older PC, Altos 600 Server), Award BIOS (AwardBIOS) – Old Version, "
        bot.send_message(call.message.chat.id, msg)
    if call.data == "keyCtrlAltS":
        msg = "Можно встретить у не очень известных брендов"
        bot.send_message(call.message.chat.id, msg)
    if call.data == "key_CtrlAltEnter":
        msg = "Dell (Older 486 Models)"
        bot.send_message(call.message.chat.id, msg)

# Запускаем постоянный опрос бота в Телеграме
bot.polling(none_stop=True, interval=0)