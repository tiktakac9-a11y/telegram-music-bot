from telethon import TelegramClient

from app.config import API_ID, API_HASH


SESSION_NAME = "data/telegram_session"


telegram_client = TelegramClient(
    SESSION_NAME,
    API_ID,
    API_HASH
)
