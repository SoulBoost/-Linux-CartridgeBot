from aiogram.utils import executor  # сам запуск
from create_bot import dp
from database import sqlite_db

async def on_startup(_):
    print('подключение к бд...')
    sqlite_db.sql_start()


from handlers import admin, client
client.register_handler_client(dp)
admin.register_handlers_admin(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
