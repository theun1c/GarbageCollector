# хранит токен, путь к базе и прочие настройки

import os

BOT_TOKEN = os.getenv('BOT_TOKEN')

if not BOT_TOKEN:
    raise RuntimeError('BOT_TOKEN environment variable not set')