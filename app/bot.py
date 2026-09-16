from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

from app.config import BOT_TOKEN


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 ربات فعال است.\n\n"
        "سیستم پردازش موسیقی در حال آماده‌سازی است."
    )


def main():
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN تنظیم نشده است.")

    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))

    print("🤖 Bot is running...")

    application.run_polling()


if __name__ == "__main__":
    main()
