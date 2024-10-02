from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command



router = Router()


@router.message(Command("help"))
async def help_start(message: Message):
    await message.answer("qanday yordam kerak!")