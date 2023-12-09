import sqlite3

import aiogram.utils.exceptions
from aiogram import types, Dispatcher
from config import bot, DESTINATION
from const import USER_FORM_TEXT
from database.sql_commands import Database
from keyboard.inline_buttons import questionnaire_keyboard
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class RegistrationStates(StatesGroup):
    nickname = State()
    bio = State()
    geo = State()
    gender = State()
    age = State()
    photo = State()


async def registration_start(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Send me your Nickname please!"
    )
    await RegistrationStates.nickname.set()


async def load_nickname(message: types.Message,
                        state: FSMContext):
    async with state.proxy() as data:
        data['nickname'] = message.text
        print(data)
    await bot.send_message(
        chat_id=message.from_user.id,
        text="Say about yourself ? (hobby, occupation)"
    )
    await RegistrationStates.next()


async def load_biography(message: types.Message,
                         state: FSMContext):
    async with state.proxy() as data:
        data['bio'] = message.text
        print(data)
    await bot.send_message(
        chat_id=message.from_user.id,
        text="Where do u live ?"
    )
    await RegistrationStates.next()


async def load_geo(message: types.Message,
                           state: FSMContext):
    async with state.proxy() as data:
        data['geo'] = message.text
        print(data)
    await bot.send_message(
        chat_id=message.from_user.id,
        text="UR gender ?"
    )
    await RegistrationStates.next()


async def load_gender(message: types.Message,
                      state: FSMContext):
    async with state.proxy() as data:
        data['gender'] = message.text
        print(data)
    await bot.send_message(
        chat_id=message.from_user.id,
        text="How old r u ? \n"
             "(Use number)"
    )
    await RegistrationStates.next()


async def load_age(message: types.Message,
                   state: FSMContext):
    try:
        type(int(message.text))
    except ValueError:
        await bot.send_message(
            chat_id=message.from_user.id,
            text="I said digital text only!!!\n"
                 "Register again"
        )
        await state.finish()
        return

    async with state.proxy() as data:
        data['age'] = message.text
        print(data)
    await bot.send_message(
        chat_id=message.from_user.id,
        text="Send me your profile photo"
    )
    await RegistrationStates.next()


async def load_photo(message: types.Message,
                     state: FSMContext):
    db = Database()
    path = await message.photo[-1].download(
        destination_dir=DESTINATION
    )
    print(path.name)

    async with state.proxy() as data:
        with open(path.name, 'rb') as photo:
            try:
                await bot.send_photo(
                    chat_id=message.from_user.id,
                    photo=photo,
                    caption=USER_FORM_TEXT.format(
                        nickname=data['nickname'],
                        bio=data['bio'],
                        geo=data['geo'],
                        gender=data['gender'],
                        age=data['age'],
                    )
                )
            except aiogram.utils.exceptions.BadRequest:
                await bot.send_photo(
                    chat_id=message.from_user.id,
                    photo=photo,
                    caption=USER_FORM_TEXT.format(
                        nickname=data['nickname'],
                        bio=data['bio'],
                        geo=data['geo'],
                        gender=data['gender'],
                        age=data['age'],
                    )
                )
                await bot.send_message(
                    chat_id=message.from_user.id,
                    text=data['biography']
                )
            db.sql_insert_user_form_register(
                telegram_id=message.from_user.id,
                nickname=data['nickname'],
                bio=data['bio'],
                geo=data['geo'],
                gender=data['gender'],
                age=data['age'],
                photo=path.name
            )
        await bot.send_message(
            chat_id=message.from_user.id,
            text="Registration was successful🍾🎉"
        )
        await state.finish()


def register_registration_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        registration_start,
        lambda call: call.data == "registration"
    )
    dp.register_message_handler(
        load_nickname,
        state=RegistrationStates.nickname,
        content_types=['text']
    )
    dp.register_message_handler(
        load_biography,
        state=RegistrationStates.bio,
        content_types=['text']
    )
    dp.register_message_handler(
        load_geo,
        state=RegistrationStates.geo,
        content_types=['text']
    )
    dp.register_message_handler(
        load_gender,
        state=RegistrationStates.gender,
        content_types=['text']
    )
    dp.register_message_handler(
        load_age,
        state=RegistrationStates.age,
        content_types=['text']
    )
    dp.register_message_handler(
        load_photo,
        state=RegistrationStates.photo,
        content_types=types.ContentTypes.PHOTO
    )