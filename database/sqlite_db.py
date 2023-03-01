import sqlite3 as sq
from create_bot import bot

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
    base.execute('CREATE TABLE IF NOT EXISTS cartridge(name TEXT , count INT)')
    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO cartridge VALUES (?, ?)', tuple(data.values()))
        base.commit()


async def sql_read(message):
    result = "Наименование - Количество:"
    for ret in cur.execute("SELECT * FROM cartridge"):
        result += f"\n{ret[0]} - {ret[1]} шт."
    await bot.send_message(message.from_user.id, result)


async def sql_take(state):
    async with state.proxy() as data:
        cur.execute(f'UPDATE cartridge SET count = count - 1 WHERE name LIKE "%{data["nameTake"]}%"')
        base.commit()


async def sql_put(state):
    async with state.proxy() as data:
        cur.execute(f'UPDATE cartridge SET count = count + 1 WHERE name LIKE "%{data["namePut"]}%"')
        base.commit()
