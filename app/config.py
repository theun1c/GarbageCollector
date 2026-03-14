# хранит токен, путь к базе и прочие настройки

import os # для чтения из енв системы

BOT_TOKEN = os.getenv('BOT_TOKEN') # читаем с енв токен

# проверка ошибок
if not BOT_TOKEN:
    raise RuntimeError('BOT_TOKEN environment variable not set')