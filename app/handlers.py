from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message



router = Router()


@router.message(CommandStart)
async def cmd_start(message: Message):
    await message.answer(text='Привет!')

@router.message()
async def gpt_answer(message: Message):
    await message.answer(text='Я тебя не понимаю')