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

model = genai.GenerativeModel("gemini-1.5-flash")

def get_indian_vibe():

    today = datetime.now().strftime("%A")

    if today in ["Saturday", "Sunday"]:
        return "weekend cozy Indian influencer vibe, cafe mood, soft glam, relaxed energy"

    return "productive Indian lifestyle, casual fashion, realistic daily content"

async def send_update():

    vibe = get_indian_vibe()

    prompt = f"""
Create today's Instagram AI influencer content plan.

Rules:
- Indian audience focused
- Realistic middle-class lifestyle
- Soft sexy but Instagram safe
- Human realistic feel
- No luxury overload
- No fake AI look
- Gen Z Indian vibe
- Natural beauty aesthetic

Today's vibe:
{vibe}

Give:
5 post ideas.

For every post include:
1. Outfit
2. Scene
3. Pose
4. Caption
5. Hashtags
6. Best posting time
7. Detailed AI image prompt
"""

    response = model.generate_content(prompt)

    text = response.text

    await bot.send_message(
        chat_id=CHAT_ID,
        text=text[:4000]
    )

def job():
    asyncio.run(send_update())

schedule.every().day.at("08:00").do(job)

print("GEMINI AI BOT RUNNING...")

job()

while True:
    schedule.run_pending()
    time.sleep(1)
