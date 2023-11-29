import sqlite3

from aiogram import types, Dispatcher
from config import bot
from database.sql_commands import Database
from keyboard.inline_buttons import questionnaire_keyboard

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

    def register_callback_handlers(dp: Dispatcher):
        dp.register_callback_query_handler(start_questionnaire_call,
                                           lambda call: call.data == "start_questionnaire")
        dp.register_callback_query_handler(one_piece_call,
                                           lambda call: call.data == "One piece")
        dp.register_callback_query_handler(aot_call,
                                           lambda call: call.data == "Attack on titan")


def register_callback_handlers(dp):
    return None