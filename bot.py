import asyncio
from telegram import Bot

BOT_TOKEN = "8695697895:AAHaFamdjvspigHzEc0J0gwIRbGctYeHc9s"
CHAT_ID = "-1003787397285"

async def main():
    bot = Bot(token=BOT_TOKEN)
    await bot.send_message(
        chat_id=CHAT_ID,
        text="Telegram bot working ✅"
    )

asyncio.run(main())
