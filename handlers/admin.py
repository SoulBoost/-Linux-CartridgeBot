from typing import Text

from create_bot import dp, bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from database import sqlite_db


class FSMAdmin(StatesGroup):
    name = State()
    count = State()


# Добавление нового картриджа
# @dp.message_handler(commands="Добавить", state=None)
async def cm_start(message: types.Message):
    await FSMAdmin.name.set()
    await message.reply('Введите название:')


# Ответ от пользователя
# @dp.message_handler(state=FSMAdmin.name)
async def name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.reply("Количество на данный момент")


# 2 ответ
# @dp.message_handler(state=FSMAdmin.count)
async def count(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['count'] = int(message.text)

    await sqlite_db.sql_add_command(state)
    await state.finish()

# exit
@dp.message_handler(state="*", commands='exit')
@dp.message_handler(Text(equals='exit', ignore_case=True), state="*")
async def cancel(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('OK')

# Регистрация хендлеров
def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(cm_start, commands=['Добавить'], state=None)
    dp.register_message_handler(name, state=FSMAdmin.name)
    dp.register_message_handler(count, state=FSMAdmin.count)
