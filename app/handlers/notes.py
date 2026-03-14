from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

#обрабатывает сообщения и нажатия кнопок

router = Router() # создаем роутер в который будем регистрировать обработчик

@router.message(CommandStart())
async def start_handler(message: Message) -> None:
    await message.answer(
        "Отправь заметку"
    )


# Что тут важно:
# • Router — это контейнер для логики
# • @router.message(...) — говорит: “эта функция обрабатывает входящие сообщения”
# • CommandStart() — конкретно фильтр для /start
# • async def и await нужны, потому что бот работает асинхронно