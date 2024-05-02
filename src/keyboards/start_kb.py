from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class StartButton:
    RECOMMENDATIONS = "Рекомендации"
    NEW_BOOKS = "Новинки"
    PROFILE = "Профиль"


def get_start_kb():
    return ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True,
        keyboard=[
            [
                KeyboardButton(text=StartButton.RECOMMENDATIONS),
                KeyboardButton(text=StartButton.NEW_BOOKS),
            ],
            [
                KeyboardButton(text=StartButton.PROFILE),
            ],
        ],
    )
