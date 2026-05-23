from telegram import Bot
import schedule
import time
import os

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=TOKEN)

def send_message():

    text = """
🔥 TODAY AI INFLUENCER CONTENT

1️⃣ Morning mirror selfie
• Loose oversized shirt
• Sleepy vibe

2️⃣ Cafe casual look
• Black crop top
• Jeans + candid pose

3️⃣ Gym glow vibe
• Sports bra + joggers
• Mirror selfie

4️⃣ Night balcony glam
• Satin dress
• Warm city lights

5️⃣ Bedroom casual hot
• White shirt + black shorts
• Cozy apartment vibe

📈 Best Posting Time:
7:30 PM – 9:00 PM
"""

    bot.send_message(
        chat_id=CHAT_ID,
        text=text
    )

schedule.every().day.at("06:00").do(send_message)

print("BOT RUNNING...")

while True:
    schedule.run_pending()
    time.sleep(1)
