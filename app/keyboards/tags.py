# создает кнопки с тегами

# импорт типов инлайн кнопок (кнопок под текстом ответа бота)
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# функция возвращающая клавиатуру
def build_tags_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(
         # список рядов кнопок - 2 ряда по 2 кнопки пока что
        inline_keyboard=[
            [
                # то что видит юзер - то что получает бот
                InlineKeyboardButton(text="[ВАЖНОЕ]", callback_data="tag:important"),            ],
            [
                InlineKeyboardButton(text="[НА ПОТОМ]", callback_data="tag:later"),
            ],
            [
                InlineKeyboardButton(text="[ДОМ]", callback_data="tag:home"),
            ],
            [
                InlineKeyboardButton(text="[РАБОТА]", callback_data="tag:work"),
            ]
        ]
    )

    # возврат клавы
    return keyboard