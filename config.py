from aiogram import Dispatcher, Bot
from decouple import config
from handlers.admin import register_admin_handlers

TOKEN = config("TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)
DESTINATION = config("DESTINATION")

register_admin_handlers(dp)
