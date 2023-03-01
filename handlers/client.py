from aiogram import types

from create_bot import bot, Dispatcher, CHANNEL_ID
from keyboards import kb_client
from database import sqlite_db


# start help
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Author by vignatenko@rolf.ru\nВсе запросы направлять сюда.', reply_markup=kb_client)
    await message.delete()


# @dp.message_handler(commands=['Список'])  # можно разбить по категориям
async def cart_list(message: types.Message):
    await sqlite_db.sql_read(message)


async def reset(message: types.message):
    if message.text == "сброс":
        await bot.send_message(message.from_user.id, 'Выполнен сброс параметров. /start', reply_markup=kb_client)
        await message.delete()


async def stop(message: types.message):
    await message.answer('1', reply_markup=types.ReplyKeyboardRemove())


async def CartList(message: types.Message):
    await sqlite_db.sql_read_group(message)


def register_handler_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(cart_list, text='Список картриджей')
    dp.register_message_handler(reset, text="сброс")

    dp.register_message_handler(stop, commands=['stop'])

    dp.register_callback_query_handler(CartList, text='CartList')
