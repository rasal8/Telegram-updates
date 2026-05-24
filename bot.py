import asyncio
import schedule
import time
from telegram import Bot

BOT_TOKEN = "8695697895:AAHaFamdjvspigHzEc0J0gwIRbGctYeHc9s"
CHAT_ID = "-1003787397285"

bot = Bot(token=BOT_TOKEN)

async def send_update():

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
    asyncio.run(send_update())

schedule.every(1).minutes.do(job)

print("BOT RUNNING...")

while True:
    schedule.run_pending()
    time.sleep(1)
