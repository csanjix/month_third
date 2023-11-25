from aiogram.types import InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup

async def start_keyboards():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        "Start Questionnaire 🤟",
        callback_data = "start_questionnaire"
    )
    markup.add(questionnaire_button)
    return markup

async def questionnaire_keyboard():
    markup = InlineKeyboardMarkup()
    Attack_on_titan_button =InlineKeyboardButton(
        'Attack_on_titan',
        callback_data = "Attack_on_titan"
    )
    OnePiece_button = InlineKeyboardButton(
        'OnePiece 👒',
        callback_data = 'OnePiece'
    )
    markup.add(Attack_on_titan_button)
    markup.add(OnePiece_button)
    return markup