from aiogram import Bot, Dispatcher, types
from decouple import config

TOKEN = config('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
db = data_base('your_database_path.db')

async def process_message(message: types.Message):
    ban_word_predict_prob = predict_prob([message.text])

    if ban_word_predict_prob > 0.1:
        await message.delete()

        telegram_id = message.from_user.id
        count = db.get_ban_user_count(telegram_id)

        if count >= 3:
            await bot.kick_chat_member(message.chat.id, telegram_id)
        else:
            db.insert_or_update_ban_user(telegram_id)

            await bot.send_message(
                message.chat.id,
                f"User {message.from_user.id} {message.from_user.first_name} violated the rules. "
                f"Warning {count + 1}/3"
            )

dp.register_message_handler(process_message)

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)