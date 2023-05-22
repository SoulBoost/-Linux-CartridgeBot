import sqlite3 as sq
from create_bot import bot, CHANNEL_ID
from aiogram import types
from keyboards import kb1, kb_client, kb, kb2

''' base - название БД
    cur - встройка, выборка из БД
    111
  '''


# создание/подключение БД


def sql_start():
    global base, cur
    base = sq.connect('printcartridge.db')
    cur = base.cursor()
    if base:
        print("Успешно подключено")
    # base.execute('CREATE TABLE IF NOT EXISTS cartridge(name TEXT(14) , count INT (5))')
    # base.commit()


# добавление новых
async def sql_add_command(state, message):
    async with state.proxy() as data:
        try:
            cur.execute(f'SELECT * FROM cartridge WHERE name = "{data["name"]}"')
            cart = cur.fetchone()
            if cart is None:
                cur.execute('INSERT INTO cartridge VALUES (?, ?)', tuple(data.values()))
                await bot.send_message(message.from_user.id, 'Добавлено', reply_markup=kb_client)
                await bot.send_message(CHANNEL_ID,
                                       f'{message.from_user.full_name} создал новую позицию {data["name"]} с количеством {data["count"]}',
                                       reply_markup=kb)
                base.commit()
            else:
                await message.reply('Данный картридж уже занесен в базу данных. Проверьте правильность введенных '
                                    'данных.', reply_markup=kb_client)
        except OverflowError:
            print('OVERFLOW ERROR')


# действие, когда берется картридж
async def sql_take(state, message):
    async with state.proxy() as data:
        cur.execute(f'SELECT COUNT(*) FROM cartridge WHERE name LIKE "%{data["nameTake"]}%"')
        cartcount = cur.fetchone()[0]
        if cartcount < 1:
            await bot.send_message(message.from_user.id, 'Несуществующее имя, проверьте список: /list')
            return
        elif cartcount == 1:
            cur.execute(f'UPDATE cartridge SET count = count - 1 WHERE name LIKE "%{data["nameTake"]}%"')
            cur.execute(f'SELECT * FROM cartridge WHERE name LIKE "%{data["nameTake"]}%"')
            ret = cur.fetchone()
            await bot.send_message(message.from_user.id,
                                   f'Вы взяли картридж: <b>{ret[0]}</b>\nТекущее количество: <b>{ret[1]}</b>',
                                   parse_mode=types.ParseMode.HTML, reply_markup=kb_client)
            await bot.send_message(CHANNEL_ID,
                                   f'{message.from_user.full_name} взял картридж: <b>{ret[0]}</b>\nТекущее количество: <b>{ret[1]}</b>',
                                   parse_mode=types.ParseMode.HTML)
        else:
            result = ""
            cur.execute(f'SELECT * FROM cartridge WHERE name LIKE "%{data["nameTake"]}%" ')
            for a in cur.fetchall():
                result += f' - {a[0]} - {a[1]} шт.\n'
            await bot.send_message(message.from_user.id, f'Совпадение имен:\n<b>{result}</b>',
                                   parse_mode=types.ParseMode.HTML, reply_markup=kb1)  # сделать инлайн кнопку
    base.commit()


# вернули картридж
async def sql_put(state, message):
    async with state.proxy() as data:
        for ret in cur.execute(f'SELECT * FROM cartridge WHERE name LIKE "%{data["namePut"]}%"'):
            for cartcount in cur.execute(f'SELECT COUNT(*) FROM cartridge WHERE name LIKE "%{data["namePut"]}%"'):
                print(cartcount[0])
                if cartcount[0] < 2:
                    cur.execute(f'UPDATE cartridge SET count = count + "{data["countPut"]}" WHERE name LIKE "%{data["namePut"]}%" ')
                    await bot.send_message(message.from_user.id,
                                           f'Вы положили картридж: <b>{ret[0]}</b>\nТекущее количество: <b>{ret[1] + data["countPut"]}</b>',
                                           parse_mode=types.ParseMode.HTML, reply_markup=kb_client)

                    await bot.send_message(CHANNEL_ID,
                                           f'{message.from_user.full_name} положил картридж: <b>{ret[0]}</b>\nТекущее количество: <b>{ret[1] + data["countPut"]}</b>',
                                           parse_mode=types.ParseMode.HTML)
                elif cartcount[0] > 1:
                    result = ""
                    for a in cur.execute(f'SELECT * FROM cartridge WHERE name LIKE "%{data["namePut"]}%"'):
                        result += f' - {a[0]} - {a[1]} шт.\n'
                    await bot.send_message(message.from_user.id, f'Совпадение имен:\n<b>{result}</b>',
                                           parse_mode=types.ParseMode.HTML,
                                           reply_markup=kb2)  # сделать инлайн кнопку
                elif cartcount[0] < 1:
                    await bot.send_message(message.from_user.id, 'Несуществующее имя, првоерьте список: /list')
        base.commit()


# список картриджей для пользователя
async def sql_read(message):
    result = "Наименование - Количество:"
    for ret in cur.execute("SELECT * FROM cartridge"):
        result += f"\n{ret[0]} - {ret[1]} шт."
    await bot.send_message(message.from_user.id, result)


# список картриджей для группы
async def sql_read_group(message):
    result = "Наименование - Количество:"
    for ret in cur.execute("SELECT * FROM cartridge"):
        result += f"\n{ret[0]} - <u>{ret[1]}</u> <u>шт.</u>"
    await bot.send_message(CHANNEL_ID, result, parse_mode=types.ParseMode.HTML)
