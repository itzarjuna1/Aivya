import os
import time
from collections import deque

import google.generativeai as genai

import config


class Aivya:
    def __init__(self):
        self.user_chats = {}
        self.system_prompt = self.load_system_prompt()

        # Gemini config
        genai.configure(api_key=config.GEMINI_API_KEY)
        self.model = genai.GenerativeModel("gemini-2.0-flash")

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

    def _build_prompt(self, system_prompt, history):
        """
        Gemini does not use role-based messages like OpenAI.
        We convert history into a single prompt.
        """
        prompt = system_prompt + "\n\n"

        for msg in history:
            if msg["role"] == "user":
                prompt += f"User: {msg['content']}\n"
            elif msg["role"] == "assistant":
                prompt += f"Aivya: {msg['content']}\n"

        prompt += "Aivya:"
        return prompt

    def ask_question(
        self,
        user_id,
        chat_id,
        message,
        user_name=None,
        new_chat=False,
    ):
        if new_chat:
            self.clear_chat(user_id, chat_id)

        self.add_message(user_id, chat_id, "user", message)
        chat_history = self.get_chat(user_id, chat_id)

        system_prompt = (
            self.system_prompt.format(user_name=user_name)
            if user_name
            else self.system_prompt
        )

        prompt = self._build_prompt(system_prompt, chat_history)

        for attempt in range(2):
            try:
                response = self.model.generate_content(
                    prompt,
                    generation_config={
                        "temperature": 0.8,
                        "max_output_tokens": 500,
                    },
                )

                reply = response.text.strip() if response.text else None
                if reply:
                    self.add_message(user_id, chat_id, "assistant", reply)
                    return reply

            except Exception as e:
                print(
                    f"Gemini API request failed (attempt {attempt + 1}/2): {e}"
                )

            if attempt < 1:
                time.sleep(1)

        print(f"All 2 attempts failed for user {user_id}")
        return None


chatbot_api = Aivya()
