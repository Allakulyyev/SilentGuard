<p align="center">
  <img src="assets/banner.png" alt="SilentGuard Banner" width="100%">
</p>

# SilentGuard Telegram Bot

[![Python](https://img.shields.io/badge/python-3.10+-blue?style=flat&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Aiogram](https://img.shields.io/badge/Powered%20by-Aiogram%203-blueviolet?logo=telegram)](https://docs.aiogram.dev/)
[![GitHub stars](https://img.shields.io/github/stars/your_username/SilentGuard?style=social)](https://github.com/your_username/SilentGuard/stargazers)

SilentGuard is a powerful Telegram group moderation bot built with Python and Aiogram 3.  
It automatically detects and bans users who send offensive messages, have inappropriate bios, or try to impersonate admins.

## 📌 Features

-   ✅ Auto-ban users for:
    -   Blacklisted words in messages
    -   Blacklisted words in bio
    -   Suspicious names or usernames (similar to admin names)
-   🧹 Deletes the message that triggered the ban
-   🔐 Secure and easily configurable
-   💡 Lightweight and easy to set up

---

## 🚀 Technologies Used

-   **Python 3.10+**
-   [Aiogram 3](https://docs.aiogram.dev/) — Telegram Bot Framework (async)
-   [`python-dotenv`](https://pypi.org/project/python-dotenv/) — for environment config
-   Standard libraries: `logging`, `asyncio`, `difflib`, `pathlib`

---

## 📁 Project Structure

<pre>
SilentGuard/
├── bot.py
├── config.py
├── handlers.py  
├── filters.py 
├── utils.py 
├── data/
│   └── blacklist.txt  
├── assets/
│   └── banner.png
├── requirements.txt 
├── .env 
├── .gitignore
└── README.md
</pre>

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your_username/SilentGuard.git
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create .env file

```ini
BOT_TOKEN = your_telegram_bot_token
```

---

## 🧠 How It Works

### When added to a Telegram group (as admin), SilentGuard:

-   Monitors new users and messages
-   If a user joins with a suspicious name or username, they are banned
-   If a user sends a message with blacklisted words, the message is deleted and the user is banned
-   If their bio contains blacklisted content, they are also banned

---

## ✅ Example: Blacklist File (data/blacklist.txt)

```perl
# Offensive words
idiot
fool

# Spam content
free money
subscribe to my channel
```

---

## 📌 Admin Setup

-   Add the bot to your group

-   Make it an admin with permission to:

    -   Ban users
    -   Delete messages

-   Edit data/blacklist.txt to fit your needs

---

## ▶️ Running the Bot

Once everything is set up:

```bash
python bot.py
```

The bot will start polling and protecting your group.

---

## 📋 To Do – Optional Enhancements

-   **Admin command to reload blacklist at runtime**  
    Allow admins to reload the blacklist without restarting the bot.

-   **Web panel for managing blacklist**  
    Simple browser interface to view, add, or remove blacklisted words.

-   **Whitelist support**  
    Trusted users will be ignored by all filters and never banned.

-   **Anti-flood system**  
    Detect and mute or ban users who send too many messages in a short time.

---

## 📝 License

This project is open-source and available under the [MIT License](LICENSE).
