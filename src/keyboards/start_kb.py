from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from src.utils import is_admin, StartButtons


def get_start_kb(user_id):
    keyboard = [
        [
            KeyboardButton(text=StartButtons.RECOMMENDATIONS),
            KeyboardButton(text=StartButtons.NEW_BOOKS),
        ],
        [
            KeyboardButton(text=StartButtons.PROFILE),
        ],
    ]
    if is_admin(user_id):
        keyboard.append([KeyboardButton(text=StartButtons.ADMIN)])
    return ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True,
        keyboard=keyboard,
    )
