from aiogram import types

from create_bot import bot, Dispatcher
from keyboards import kb_client, kb_exit
from database import sqlite_db

#start help
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Author by vignatenko@rolf.ru', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('dSDAsp[ldaps[la[kE{WAEK@#')


# @dp.message_handler(commands=['Список'])  # можно разбить по категориям
async def cart_list(message: types.Message):
    await sqlite_db.sql_read(message)


async def put_cart(message: types.Message):
    await sqlite_db.sql_put(message)


# @dp.message_handler()
async def echo(message: types.message):
    if message.text == "exit":
        await bot.send_message(message.from_user.id, 'Выход ', reply_markup = kb_client)


def register_handler_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(cart_list, text= 'Список картриджей')
    dp.register_message_handler(put_cart, text='Взять')
    dp.register_message_handler(echo, text = "exit")
