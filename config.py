from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "35279715"))
API_HASH = getenv("API_HASH", "b4c339216397b5941d88c8617d2dc12b")
BOT_TOKEN = getenv("BOT_TOKEN", "")

OWNER_ID = int(getenv("OWNER_ID", "7651303468"))

LOGGER_ID = int(getenv("LOGGER_ID", "-1003228624224"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://knight4563:knight4563@cluster0.a5br0se.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

GEMINI_API_KEY = getenv("GEMINI_API_KEY", "")
GEMINI_MODEL = getenv("GEMINI_MODEL", "gemini-2.0-flash")
