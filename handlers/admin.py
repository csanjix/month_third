from aiogram import types, Dispatcher
from config import bot
from database.sql_commands import Database

async def show_all_users(message: types.Message):
    db = Database()
    users = db.sql_select_user()
    users_info = "\n".join([f"{user['username']} ({user['first_name']} {user['last_name']})" for user in users])
    await bot.send_message(message.chat.id, f"All users:\n{users_info}")

async def show_potential_bans(message: types.Message):
    db = Database()
    potential_bans = db.sql_select_potential_bans()
    bans_info = "\n".join([f"{user['username']} ({user['first_name']} {user['last_name']}), Bans: {user['ban_count']}" for user in potential_bans])
    await bot.send_message(message.chat.id, f"Potential bans:\n{bans_info}")

async def warn_potential_bans(message: types.Message):
    db = Database()
    potential_bans = db.sql_select_potential_bans()
    for user in potential_bans:
        user_id = user['telegram_id']
        count = user['ban_count']
        if count >= 3:
            await bot.send_message(user_id, "Warning: You've been flagged for inappropriate behavior. "
                                            "Continued violations may result in a ban.")


def register_admin_handlers(dp: Dispatcher):
    dp.register_message_handler(show_all_users, commands=['show_all_users'], is_admin=True)
    dp.register_message_handler(show_potential_bans, commands=['show_potential_bans'], is_admin=True)
    dp.register_message_handler(warn_potential_bans, commands=['warn_potential_bans'], is_admin=True)
