import asyncio
import schedule
import time
import os
from datetime import datetime
from telegram import Bot
from openai import OpenAI

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

bot = Bot(token=BOT_TOKEN)

client = OpenAI(
    api_key=OPENAI_API_KEY
)

def get_indian_vibe():

    today = datetime.now().strftime("%A")

    if today in ["Saturday", "Sunday"]:
        mood = "weekend chill, cafe, soft glam, relaxed Indian influencer vibe"
    else:
        mood = "productive lifestyle, casual fashion, realistic Indian daily life"

    return mood

async def send_update():

    mood = get_indian_vibe()

    prompt = f"""
Create today's AI influencer content plan for Indian Instagram audience.

Rules:
- Realistic Indian girl influencer
- Neutral middle-class realism
- Not overly luxury
- Not too glamorous
- Instagram-safe attractive vibe
- Soft sensual energy allowed
- Human realistic feel
- No AI-looking content
- Modern Gen Z Indian audience
- Outfit + pose + expression + lighting
- Include captions
- Include best posting times
- Include hashtags

Today's mood:
{mood}

Give:
5 Instagram post ideas.
"""

    response = client.chat.completions.create(
        model="gpt-5.5",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    text = response.choices[0].message.content

    await bot.send_message(
        chat_id=CHAT_ID,
        text=text[:4000]
    )

def job():
    asyncio.run(send_update())

schedule.every().day.at("08:00").do(job)

print("AI BOT RUNNING...")

job()

while True:
    schedule.run_pending()
    time.sleep(1)
