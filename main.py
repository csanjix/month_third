from aiogram import Bot, Dispatcher, types
from decouple import config
from database import data_base
from aiogram import executor

async def show_all_users(message: types.Message):
    users = db.get_all_users()
    text = "List of all users:\n"
    for user in users:
        text += f"{user['id']}. {user['username']} ({user['first_name']} {user['last_name']})\n"
    await message.answer(text)

async def show_potential_bans(message: types.Message):
    potential_bans = db.get_potential_bans()
    text = "Users with potential bans:\n"
    for ban in potential_bans:
        text += f"{ban['id']}. {ban['username']} ({ban['first_name']} {ban['last_name']}) - Violations: {ban['count']}\n"
    await message.answer(text)

async def send_warning_to_potential_bans(message: types.Message):
    potential_bans = db.get_potential_bans()
    for ban in potential_bans:
        user_id = ban['telegram_id']
        count = ban['count']
        warning_text = f"You have been warned! You have {count} violations. After 3 violations you will be banned."
        await Bot.send_message(user_id, warning_text)

async def admin_menu_callback_handler(callback_query: types.CallbackQuery):
    await Bot.answer_callback_query(callback_query.id)
    await Bot.edit_message_text(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        text="Admin menu",
        reply_markup=admin_menu_keyboard()
    )

async def admin_menu_button_handler(callback_query: types.CallbackQuery):
    if callback_query.data == 'show_all_users':
        await show_all_users(callback_query.message)
    elif callback_query.data == 'show_potential_bans':
        await show_potential_bans(callback_query.message)
    elif callback_query.data == 'send_warning_to_potential_bans':
        await send_warning_to_potential_bans(callback_query.message)
    else:
        await Bot.answer_callback_query(callback_query.id, text="Something went wrong")

def admin_menu_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    buttons = [
        types.InlineKeyboardButton("Show all users", callback_data='show_all_users'),
        types.InlineKeyboardButton("Show potential bans", callback_data='show_potential_bans'),
        types.InlineKeyboardButton("Send warning to potential bans", callback_data='send_warning_to_potential_bans'),
    ]
    keyboard.add(*buttons)
    return keyboard

dp.register_message_handler(admin_menu_callback_handler, commands=['admin_menu'])

dp.register_callback_query_handler(admin_menu_button_handler, lambda callback_query: callback_query.data.startswith('admin_menu'))

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)