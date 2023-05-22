from create_bot import dp, bot, CHANNEL_ID
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from database import sqlite_db
from keyboards import kb_client, kb_exit, kb, kb1


# exit 1
@dp.message_handler(state="*", commands='exit')
@dp.message_handler(Text(equals='exit', ignore_case=True), state="*")
async def cancel(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('OK', reply_markup=kb_client)


class TakeCart(StatesGroup):
    nameTake = State()


#взять картридж
async def take_start(message: types.Message):
    await TakeCart.nameTake.set()
    await bot.send_message(message.from_user.id, "Укажите номер картриджа: ", reply_markup=kb_exit)


async def getname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['nameTake'] = message.text.upper()
    await sqlite_db.sql_take(state, message)
    await state.finish()


# Вернуть картридж
class PutCart(StatesGroup):
    namePut = State()
    countPut = State()


async def put_start(message: types.Message):
    await PutCart.namePut.set()
    await bot.send_message(message.from_user.id, "Укажите номер картриджа: ", reply_markup=kb_exit)


async def getputname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['namePut'] = message.text.upper()
    await PutCart.next()
    await message.reply("Количество", reply_markup=kb_exit)


async def count_put(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            data['countPut'] = int(message.text)
        except ValueError:
            await message.reply('Неверное значение')
            return
    await sqlite_db.sql_put(state, message)
    await state.finish()


# Добавление нового картриджа
class FSMAdmin(StatesGroup):
    name = State()
    count = State()


async def cm_start(message: types.Message):
    await FSMAdmin.name.set()
    await message.reply('Введите название:', reply_markup=kb_exit)


# Ответ от пользователя
async def name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text.upper()
    await FSMAdmin.next()
    await message.reply("Количество на данный момент", reply_markup=kb_exit)


# 2 ответ
async def count(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            data['count'] = int(message.text)
            if (data['count'] > 100) or (data['count'] < 0):
                await message.reply('Неверное количество, введите повторно: ')
                return
        except ValueError:
            await message.reply('Только числовое значение', reply_markup=kb_exit)
            return
    await sqlite_db.sql_add_command(state, message)
    await state.finish()


# Регистрация хендлеров
def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(cm_start, text='Добавить новый', state=None)
    dp.register_message_handler(name, state=FSMAdmin.name)
    dp.register_message_handler(count, state=FSMAdmin.count)

    dp.register_callback_query_handler(take_start, text='rec', state = None)
    dp.register_message_handler(take_start, text='Взять', state=None)
    dp.register_message_handler(getname, state=TakeCart.nameTake)

    dp.register_callback_query_handler(put_start, text='rec1', state=None)
    dp.register_message_handler(put_start, text='Положить', state=None)
    dp.register_message_handler(getputname, state=PutCart.namePut)
    dp.register_message_handler(count_put, state=PutCart.countPut)
