import time
import os
from asyncio import to_thread

import google.generativeai as genai
from pyrogram import filters
from pyrogram.enums import ChatAction
from pyrogram.types import Message

from src import app

# ───────────────── CONFIG ───────────────── #

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

MODEL = genai.GenerativeModel("gemini-2.0-flash")

user_message_tracker = {}
triggered_words = ["aivya", "baby"]

SYSTEM_PROMPT = (
    "You are Aivya, a friendly, flirty, playful AI chatbot. "
    "Reply short, natural, and human-like. "
    "Do not mention you are an AI unless asked."
)

# ───────────────── FILTER ───────────────── #

def chatbot_filter_func(_, __, m: Message):
    if not m.text or not m.from_user or m.from_user.is_bot:
        return False

    text = m.text.lower()
    user_id = m.from_user.id
    current_time = time.time()

    if not any(word in text for word in triggered_words) and not m.mentioned:
        return False

    if text.startswith(("!", "/")) or m.via_bot or m.sticker:
        return False

    history = user_message_tracker.get(user_id, [])
    history = [t for t in history if current_time - t < 1]

    if len(history) >= 2:
        return False

    history.append(current_time)
    user_message_tracker[user_id] = history
    return True


chatbot_filter = filters.create(chatbot_filter_func)

# ───────────────── GEMINI CALL ───────────────── #

def ask_gemini(question: str, user_name: str):
    prompt = f"""
{SYSTEM_PROMPT}

User name: {user_name}
User message: {question}

Reply as Aivya:
"""
    response = MODEL.generate_content(prompt)
    return response.text.strip() if response and response.text else None


# ───────────────── HANDLER ───────────────── #

@app.on_message(filters.text & filters.group & chatbot_filter)
async def mention_chatbot(_, message: Message):
    await app.send_chat_action(message.chat.id, ChatAction.TYPING)

    question = message.text
    user_name = " ".join(
        part
        for part in [message.from_user.first_name, message.from_user.last_name]
        if part
    )

    reply = await to_thread(ask_gemini, question, user_name)

    if not reply:
        await message.reply_text(
            f"⚠️ {app.name} is currently unavailable. Please try again later."
        )
    else:
        await message.reply_text(reply)
