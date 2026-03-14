import asyncio # нужен для запуска асинхронной функции main

# Bot - TG API  Dispatcher - маршрутизатор входящих событий
from aiogram import Bot, Dispatcher

# просто импорты функционала и токена из файлов
from config import BOT_TOKEN
from handlers.notes import router # импорт роутера с обработчиком команд

# собирает приложение и запускает бота

# главная функция асинхронная
async def main() -> None:
    bot = Bot(token=BOT_TOKEN) # инициализируем бота
    dispatcher = Dispatcher() # создаем диспатчер который принимает события от тг

    dispatcher.include_router(router) # подключаем роутер с обработчиками

    try:
        # переключение на поллинг - клиент периодически отправляет запросы
        await bot.delete_webhook(drop_pending_updates=True)
        # запуск постоянного чтения из тг
        await dispatcher.start_polling(bot)
    finally:
        await bot.session.close()  # гарантия закрытия бота

if __name__ == '__main__': # блок выполняется если файл запущен напрямую
    asyncio.run(main()) # старт event loop и выполнение main