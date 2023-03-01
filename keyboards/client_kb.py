from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup

b1 = KeyboardButton('Список картриджей')
b2 = KeyboardButton('Взять')
b4 = KeyboardButton('Положить')
b3 = KeyboardButton('Добавить новый')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.add(b1).add(b2).insert(b4).add(b3)


b5 = KeyboardButton('exit')
kb_exit = ReplyKeyboardMarkup(resize_keyboard=True)
kb_exit.add(b5)

#Кнопки
kb = InlineKeyboardMarkup(row_width=2)
inline_kb = InlineKeyboardButton(text="Список картриджей", callback_data='CartList')
kb.add(inline_kb)
