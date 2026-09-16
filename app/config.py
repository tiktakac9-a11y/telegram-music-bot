import os


BOT_TOKEN = os.getenv("BOT_TOKEN", "")

SOURCE_CHANNEL = os.getenv("SOURCE_CHANNEL", "")
DESTINATION_CHANNEL = os.getenv("DESTINATION_CHANNEL", "")

START_DATE = os.getenv("START_DATE", "2026-09-05")

SCHEDULE_1 = os.getenv("SCHEDULE_1", "10:00")
SCHEDULE_2 = os.getenv("SCHEDULE_2", "15:00")
SCHEDULE_3 = os.getenv("SCHEDULE_3", "20:00")

BRAND_USERNAME = os.getenv("BRAND_USERNAME", "")

COVER_PATH = os.getenv(
    "COVER_PATH",
    "assets/cover.jpg"
)
