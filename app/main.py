import asyncio # нужен для запуска асинхронной функции main

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from handlers.notes import router

# собирает приложение и запускает бота

async def main() -> None:
    bot = Bot(token=BOT_TOKEN)
    dispatcher = Dispatcher() # создаем диспатчер который принимает события от тг

    dispatcher.include_router(router) # подключаем роутер с обработчиками

    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dispatcher.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__': # блок выполняется если файл запущен напрямую
    asyncio.run(main())