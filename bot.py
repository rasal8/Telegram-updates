from telegram import Bot
import schedule
import time
import os
import asyncio

TOKEN = os.getenv("8695697895:AAHaFamdjvspigHzEc0J0gwIRbGctYeHc9s")
CHAT_ID = os.getenv("-1003787397285")

bot = Bot(token=TOKEN)

async def send_message():

    text = """
🔥 TODAY AI INFLUENCER CONTENT

1️⃣ Morning mirror selfie
2️⃣ Cafe casual look
3️⃣ Gym glow vibe
4️⃣ Night balcony glam
5️⃣ Bedroom casual hot

📈 Best Posting Time:
7:30 PM – 9:00 PM
"""

    await bot.send_message(
        chat_id=CHAT_ID,
        text=text
    )

def job():
    asyncio.run(send_message())

schedule.every().day.at("06:00").do(job)

print("BOT RUNNING...")

while True:
    schedule.run_pending()
    time.sleep(1)
