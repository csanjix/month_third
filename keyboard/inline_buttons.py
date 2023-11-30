from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
async def start_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        "Start Questionnaire 🤟",
        callback_data="start_questionnaire"
    )
    registration_button = InlineKeyboardButton(
        'Registration 🤌',
        callback_data='registration'
    )
    markup.add(questionnaire_button)
    markup.add(registration_button)
    return markup

async def questionnaire_keyboard():
    markup = InlineKeyboardMarkup()
    one_piece_button = InlineKeyboardButton(
        "One piece 👒",
        callback_data="One piece"
    )
    atack_on_titan_button = InlineKeyboardButton(
        "Attack on titan 🐋",
        callback_data="Attack on titan"
    )
    markup.add(one_piece_button)
    markup.add(atack_on_titan_button)
    return markup