from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage #хранит данные в ОЗУ локалки

import os
# добавление from settings import TOKEN, CHANNEL_ID
# -1001690773499
storage = MemoryStorage()

bot = Bot('5776400621:AAFlZH01YpqKvpoM5r-DxTGAZYLyFA_sXQU')
CHANNEL_ID = ('-878294496')
dp = Dispatcher(bot, storage=storage)
print(bot)
#print(CHANNEL_ID)
