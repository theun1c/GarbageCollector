from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

# импорт функции инлайн кнопок
from keyboards.tags import build_tags_keyboard

#обрабатывает сообщения и нажатия кнопок

router = Router() # создаем роутер в который будем регистрировать обработчик

@router.message(CommandStart())
async def start_handler(message: Message) -> None:
    await message.answer(
        "Тебя приветствует коллекционер мусорных заметок! Пиши все что хочешь..."
    )

# Что тут важно:
# • Router — это контейнер для логики
# • @router.message(...) — говорит: “эта функция обрабатывает входящие сообщения”
# • CommandStart() — конкретно фильтр для /start
# • async def и await нужны, потому что бот работает асинхронно

# выдача кнопок тегов если что то написали
@router.message(F.text & ~F.text.startswith("/"))
async def note_handler(message: Message) -> None:
    text = message.text.strip()
    if not text:
        await message.answer("Нельзя сохранить пустую заметку")
        return

    await message.answer(
    "Выбери тег для заметки",
        reply_markup=build_tags_keyboard()
    )

# получаем наименование тега
@router.callback_query(F.data.startswith("tag:"))
async def tag_handler(callback: CallbackQuery) -> None:
    if callback.message is None:
        await callback.answer()
        return

    tag_code = callback.data.split(":", maxsplit=1)[1]

    tag_names = {
        "important": "ВАЖНОЕ",
        "later": "НА ПОТОМ",
        "home": "ДОМ",
        "work": "РАБОТА",
    }
    tag_name = tag_names.get(tag_code, tag_code)

    await callback.message.edit_reply_markup(reply_markup=None)
    await callback.message.answer(f"Выбран тег: {tag_name}")
    await callback.answer()