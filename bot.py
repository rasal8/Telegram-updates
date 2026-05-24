import asyncio
import schedule
import time
import os
from datetime import datetime
from telegram import Bot
import google.generativeai as genai

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

bot = Bot(token=BOT_TOKEN)

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("models/gemini-1.5-flash")

def get_indian_vibe():

    today = datetime.now().strftime("%A")

    if today in ["Saturday", "Sunday"]:
        return "weekend cozy Indian influencer vibe, cafe mood, soft glam, relaxed energy"

    return "productive Indian lifestyle, casual fashion, realistic daily content"

async def send_update():

    vibe = get_indian_vibe()

    prompt = f"""
Create 3 Indian Instagram influencer content ideas.

Rules:
- Realistic Indian influencer
- Middle-class realistic vibe
- Soft sexy but Instagram safe
- Human realistic feel
- No luxury overload
- Gen Z Indian audience

Today's vibe:
{vibe}

For every post include:
- Outfit
- Pose
- Caption
- Hashtags
- Best posting time
- Detailed AI image prompt
"""

    response = model.generate_content(prompt)

    text = response.text[:3500]

    await bot.send_message(
        chat_id=CHAT_ID,
        text=text
    )

def job():
    asyncio.run(send_update())

schedule.every().day.at("08:00").do(job)

print("GEMINI AI BOT RUNNING...")

job()

while True:
    schedule.run_pending()
    time.sleep(1)
