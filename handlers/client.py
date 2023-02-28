from aiogram import types

from create_bot import bot, Dispatcher
from keyboards import kb_client
from database import sqlite_db

# @dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Author', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('dSDAsp[ldaps[la[kE{WAEK@#')


# @dp.message_handler(commands=['Список'])  # можно разбить по категориям
async def cart_list(message: types.Message):
    await sqlite_db.sql_read(message)

# @dp.message_handler()
async def echo(message: types.message):
    if message.text == "Информация":
        await bot.send_message(message.from_user.id, 'Какая - то информация')


def register_handler_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(cart_list, commands=['Список'])