<h1 align="center">✨ Aivya AI ✨</h1>

<p align="center">
Aivya is a friendly Telegram chatbot powered by OpenAI built with Python and Pyrogram to chat naturally, listen, and support conversations in private and group chats. 🤖💬
</p>

## ⚙️ Prerequisites
- Python 3.13+
- MongoDB database
- Telegram Bot Token from [@BotFather](https://t.me/BotFather)
- Telegram API credentials from [my.telegram.org](https://my.telegram.org/apps)
- OpenAI API key from [platform.openai.com](https://platform.openai.com/api-keys)


## 🛠️ Installation

### Local Setup
1. **Clone the repository**
```bash
git clone https://github.com/yourusername/Aivya.git
cd Aivya
```

2. **Create and activate virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment variables**
```bash
cp example.env .env
```

Edit `.env` file with your credentials:
```env
API_ID=your_api_id
API_HASH=your_api_hash
BOT_TOKEN=your_bot_token
LOGGER_ID=your_logger_channel_id
MONGO_URL=your_mongodb_url
OWNER_ID=your_telegram_user_id
OPENAI_API_KEY=your_openai_api_key
```

5. **Run the bot**
```bash
bash start
```
### Deploy to Heroku
Click the button below to deploy Aivya on Heroku:

<a href="https://dashboard.heroku.com/new?template=https://github.com/MaybeChiku/Aivya">
    <img src="https://img.shields.io/badge/Deploy%20On%20Heroku-black?style=for-the-badge&logo=heroku"/>
</a>



## Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `API_ID` | Telegram API ID from my.telegram.org | Yes |
| `API_HASH` | Telegram API Hash from my.telegram.org | Yes |
| `BOT_TOKEN` | Bot token from @BotFather | Yes |
| `MONGO_URL` | MongoDB connection string | Yes |
| `LOGGER_ID` | Telegram channel/group ID for logging | Yes |
| `OWNER_ID` | Your Telegram user ID | Yes |
| `OPENAI_API_KEY` | OpenAI API key | Yes |
| `OPENAI_MODEL` | OpenAI model to use (default: gpt-4o-mini) | No |


## 🗣️ Trigger Words
By default, Aivya responds when:
- The bot is mentioned in a group
- Messages include trigger words: "aivya" or "baby"

These can be customized in `src/modules/aivya.py`.

### Example Usage
- "Hey aivya, how are you?"
- Replying directly to the bot’s messages

## 🧠 Customize AI Personality
Edit `src/utils/prompt.txt` to customize Aivya's personality, tone, and behavior.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

If you encounter any issues or have questions:
- 💬 Join our [Telegram Support Group](https://t.me/DebugAngels)
- 🐛 Open an issue on GitHub
- 📧 Contact the maintainer via Telegram

## Acknowledgments

- [Pyrogram](https://github.com/KurimuzonAkuma/pyrogram) - Telegram MTProto API framework
- [OpenAI](https://openai.com/) - AI language models
- [Motor](https://github.com/mongodb/motor) - Async MongoDB driver

⭐ If you find this project helpful, please consider giving it a star on GitHub.