# pip install python-telegram-bot
# pip install python-dotenv

import os
import logging
import telegram
from dotenv import load_dotenv
import asyncio

load_dotenv()

TELEGRAM_BOT_TOKEN= os.getenv("TELEGRAM_BOT_TOKEN")
YOUR_PERSONAL_CHAT_ID= os.getenv("YOUR_PERSONAL_CHAT_ID")

# Настройка логирования
logging.basicConfig(level=logging.DEBUG)

async def send_telegram_message(token, chat_id, message, parse_mode="Markdown"):
    try:
        bot = telegram.Bot(token=token)
        await bot.send_message(chat_id=chat_id, text=message, parse_mode=parse_mode)
        logging.info(f'Сообщение "{message}" отправлено в чат {chat_id}')
    except Exception as e:
        logging.error(f'Ошибка отправки сообщения в чат {chat_id}: {e}')


# Отправка сообщения в телеграм
message = """
*Привет, группа Python331!*
Это сообщение отправлено из Python-скрипта с использованием библиотеки python-telegram-bot.

```python
print("Hello, Python331!")
```
"""

asyncio.run(send_telegram_message(TELEGRAM_BOT_TOKEN, YOUR_PERSONAL_CHAT_ID, message))