import sqlite3
import re
from aiogram import types, Dispatcher
from config import bot, ADMIN_ID
from database.sql_commands import Database
from keyboard.inline_buttons import questionnaire_keyboard
from scraping.async_scraper import AsyncScraper
from keyboard.inline_buttons import save_button
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


async def async_scraper_call(call: types.CallbackQuery):
    data = await AsyncScraper().async_scrapers()
    links = AsyncScraper
    for link in data:
        await bot.send_message(chat_id=call.from_user.id, text=f"{link}", reply_markup=await save_button())


async def save_service_call(call: types.CallbackQuery):
    link = re.search(r'(https?://\S+)', call.message.text)
    if link:
        Database().sql_insert_service_commands(link=link.group(0))

    await bot.send_message(chat_id=call.from_user.id, text="U save link")


def register_callback_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(start_questionnaire_call,
                                       lambda call: call.data == "start_questionnaire")
    dp.register_callback_query_handler(one_piece_call,
                                       lambda call: call.data == "one piece")
    dp.register_callback_query_handler(aot_call,
                                       lambda call: call.data == "attack on titan")
    dp.register_message_handler(admin_call,
                                lambda word: "dorei" in word.text)

    dp.register_callback_query_handler(async_scraper_call,
                                       lambda call: call.data == 'async_news')
    dp.register_callback_query_handler(save_service_call,
                                       lambda call: call.data == 'save_service')