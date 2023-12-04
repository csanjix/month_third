import sqlite3

from aiogram import types, Dispatcher
from config import bot, ADMIN_ID
from database.sql_commands import Database
from keyboard.inline_buttons import questionnaire_keyboard
from scraping.scraper import NewsScraper

async def start_questionnaire_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="One piece or Attack on titan ?",
        reply_markup=await questionnaire_keyboard()
    )
async def one_piece_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="You are One piece fan"
    )
async def aot_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="You are AOT fan"
    )

async def admin_call(message: types.Message):
    print(ADMIN_ID)
    print(message.from_user.id)
    if message.from_user.id == int(ADMIN_ID):
        await message.delete()
        await bot.send_message(
            chat_id=message.from_user.id,
            text='Hello 👋'
        )
    else:
        await bot.send_message(
            chat_id=message.from_user.id,
            text='Who R U 🤔 ?'
        )

async def scraper_call(call: types.CallbackQuery):
    scraper = NewsScraper()
    data = scraper.parse_data()
    for url in data[:4]:
        await bot.send_message(
            chat_id=call.from_user.id,
            text=f"{scraper.PLUS_URL + url}"
        )

def register_callback_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(start_questionnaire_call,
                                       lambda call: call.data == "start_questionnaire")
    dp.register_callback_query_handler(one_piece_call,
                                       lambda call: call.data == "One piece")
    dp.register_callback_query_handler(aot_call,
                                       lambda call: call.data == "Attack on titan")
    dp.register_message_handler(admin_call, lambda word: 'dorei' in word.text)

    dp.register_callback_query_handler(scraper_call,
                                       lambda call: call.data == "news")
