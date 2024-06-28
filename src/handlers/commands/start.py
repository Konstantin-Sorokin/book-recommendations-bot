from aiogram import Router, types
from aiogram.filters import CommandStart

from src.keyboards.start_kb import get_start_kb

router = Router(name=__name__)


@router.message(CommandStart())
async def handle_start_command(message: types.Message):
    await message.answer(
        text="Hello",
        reply_markup=get_start_kb(message.from_user.id),
    )
