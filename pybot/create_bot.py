from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage #хранит данные в ОЗУ локалки

storage = MemoryStorage()

bot = Bot(token='6260963136:AAFJwoXxG_C5jbM2NJaSyugAi7AS4yaTeMg')
CHANNEL_ID = 6260963136
dp = Dispatcher(bot, storage=storage)