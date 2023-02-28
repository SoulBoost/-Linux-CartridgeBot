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
    for ret in cur.execute('SELECT * FROM cartridge').fetchall():
        await bot.send_message(message.from_user.id, f'Наименование - Количествоо:\n {ret[0]} - {ret[1]} штук')
    # cur.execute('SELECT * FROM cartridge')
    # sql = cur.fetchall()
    # await bot.send_message(message.from_user.id, sql)