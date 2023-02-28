from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage #хранит данные в ОЗУ локалки

storage = MemoryStorage()

bot = Bot(token='6260963136:AAFJwoXxG_C5jbM2NJaSyugAi7AS4yaTeMg')
dp = Dispatcher(bot, storage=storage)