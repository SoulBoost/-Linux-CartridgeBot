"""
Есть два варианта выбора.
1 - пользователь выбирает номер картриджа, далее выбирает что с ним делать - лучше так. Так как при пополнении огромных запасов, проще будет много раз + прожать.
2  - сначала действие, потом картридж.


Уведомление о том, что взяли, положили - приходит в общую группу.
    Пример: [Был взят картирдж cf410x - 1 штука] - Вывести весь список картриджей
Сделать проверку при добавлении нового картриджа
Возможность редактировать каждый картридж отдельно
Название кнопок +
Проверка при "Взять" и "Положить".

Добавление триггеров при низком количестве картриджей (желательно также в группу)

"""

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
