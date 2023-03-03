import sqlite3 as sq
from create_bot import bot, CHANNEL_ID
from aiogram import types

''' base - название БД
    cur - встройка, выборка из БД
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


async def sql_add_command(state, message):
    async with state.proxy() as data:
        try:
            cur.execute(f'SELECT * FROM cartridge WHERE name = "{data["name"]}"')
            cart = cur.fetchone()
            if cart is None:
                cur.execute('INSERT INTO cartridge VALUES (?, ?)', tuple(data.values()))
                base.commit()
            else:
                await message.reply('Данный картридж уже занесен в базу данных. Проверьте правильность введенных '
                                    'данных.')
        except OverflowError:
            print('OVERFLOW ERROR')


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

# действие, когда берется картридж
async def sql_take(state):
    async with state.proxy() as data:
        for ret in cur.execute(f'SELECT cartridge WHERE name LIKE "%{data["nameTake"]}"'):
            print(ret)
        cur.execute(f'UPDATE cartridge SET count = count - 1 WHERE name LIKE "%{data["nameTake"]}%"')
        base.commit()

# вернули картридж
async def sql_put(state, p):
    async with state.proxy() as data:
        cur.execute(f'UPDATE cartridge SET count = "{data["countPut"]}" WHERE name LIKE "%{data["namePut"]}%"')
        base.commit()
