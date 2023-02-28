from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/Список')

b2 = KeyboardButton('Взять картридж')
b3 = KeyboardButton('Положить катридж')

b4 = KeyboardButton('/Добавить')
b5 = KeyboardButton('exit')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).add(b2).insert(b3).add(b4).add(b5)

