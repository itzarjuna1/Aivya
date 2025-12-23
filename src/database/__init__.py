from .chats import *
from motor.motor_asyncio import AsyncIOMotorClient

import config

# Asynchronous Database Connection
ChatBot = AsyncIOMotorClient(config.MONGO_URL)
# Database
db = ChatBot["Avira"]

# Collections
usersdb = db["users"]  # Users Collection
chatsdb = db["chats"]  # Chats Collection

# Importing other modules
