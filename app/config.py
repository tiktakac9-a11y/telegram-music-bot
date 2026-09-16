import os


# Telegram Bot
BOT_TOKEN = os.getenv("BOT_TOKEN", "")


# Telegram API
API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH", "")


# Channels
SOURCE_CHANNEL = os.getenv("SOURCE_CHANNEL", "")
DESTINATION_CHANNEL = os.getenv("DESTINATION_CHANNEL", "")


# Processing
START_DATE = os.getenv("START_DATE", "2026-09-05")


# Daily schedule
SCHEDULE_1 = os.getenv("SCHEDULE_1", "10:00")
SCHEDULE_2 = os.getenv("SCHEDULE_2", "15:00")
SCHEDULE_3 = os.getenv("SCHEDULE_3", "20:00")


# Channel username / brand
BRAND_USERNAME = os.getenv("BRAND_USERNAME", "")


# Cover
COVER_PATH = os.getenv(
    "COVER_PATH",
    "assets/cover.jpg"
)


# Database
DATABASE_URL = os.getenv("DATABASE_URL", "")
