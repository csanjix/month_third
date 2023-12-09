from aiogram import Dispatcher, Bot
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage


proxy_url = "http://proxy.server:3128"
storage = MemoryStorage()
TOKEN = config("TOKEN")
bot = Bot(token=TOKEN, proxy=proxy_url)
dp = Dispatcher(bot=bot, storage=storage)
DESTINATION = config("DESTINATION")
ADMIN_ID = int(config("ADMIN_ID"))