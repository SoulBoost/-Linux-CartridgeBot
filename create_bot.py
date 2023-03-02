from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage #хранит данные в ОЗУ локалки
# -1001690773499
storage = MemoryStorage()

bot = Bot(token='5655353500:AAHeMfLZ_cLwKJU8kPFjn9dn-y5loWAWZXw', parse_mode="HTML")
CHANNEL_ID = '-1001762333718'
dp = Dispatcher(bot, storage=storage)