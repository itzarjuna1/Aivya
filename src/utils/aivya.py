import os
from collections import deque
from openai import OpenAI
import config

class Aivya:
    def __init__(self):
        self.user_chats = {}
        self.system_prompt = self.load_system_prompt()
        self.client = OpenAI(api_key=config.OPENAI_API_KEY)
        self.model = config.OPENAI_MODEL

    def load_system_prompt(self):
        base_dir = os.path.dirname(__file__)
        prompt_path = os.path.join(base_dir, "prompt.txt")
        with open(prompt_path, "r", encoding="utf-8") as f:
            return f.read().strip()

    def _get_key(self, user_id, chat_id):
        return f"{user_id}:{chat_id}"

    def get_chat(self, user_id, chat_id):
        key = self._get_key(user_id, chat_id)
        if key not in self.user_chats:
            self.user_chats[key] = deque(maxlen=10)
        return list(self.user_chats[key])

    def add_message(self, user_id, chat_id, role, content):
        key = self._get_key(user_id, chat_id)
        if key not in self.user_chats:
            self.user_chats[key] = deque(maxlen=10)
        self.user_chats[key].append({"role": role, "content": content})

    def clear_chat(self, user_id, chat_id):
        key = self._get_key(user_id, chat_id)
        if key in self.user_chats:
            self.user_chats[key].clear()

    def ask_question(self, user_id, chat_id, message, user_name=None, new_chat=False):
        if new_chat:
            self.clear_chat(user_id, chat_id)
        self.add_message(user_id, chat_id, "user", message)
        chat_history = self.get_chat(user_id, chat_id)
        if user_name:
            system_prompt = self.system_prompt.format(user_name=user_name)
        else:
            system_prompt = self.system_prompt
        for attempt in range(2):
            try:
                messages = [{"role": "system", "content": system_prompt}] + chat_history
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=messages,
                    temperature=0.8,
                    max_tokens=500
                )
                reply = response.choices[0].message.content.strip()
                if reply:
                    self.add_message(user_id, chat_id, "assistant", reply)
                    return reply
            except Exception as e:
                print(f"OpenAI API request failed (attempt {attempt + 1}/2): {e}")
            if attempt < 1:
                import time
                time.sleep(1)
        print(f"All 2 attempts failed for user {user_id}")
        return None

chatbot_api = Aivya()