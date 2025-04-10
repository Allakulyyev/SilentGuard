<p align="center">
  <img src="assets/banner.png" alt="SilentGuard Banner" width="100%">
</p>

# SilentGuard Telegram Bot

🌐 [🇺🇸 English](README.md)

[![Python](https://img.shields.io/badge/python-3.10+-blue?style=flat&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Aiogram](https://img.shields.io/badge/Powered%20by-Aiogram%203-blueviolet?logo=telegram)](https://docs.aiogram.dev/)
[![GitHub stars](https://img.shields.io/github/stars/Allakulyyev/SilentGuard?style=social)](https://github.com/Allakulyyev/SilentGuard/stargazers)

SilentGuard — это мощный бот модерации групп в Telegram, созданный на Python с использованием Aiogram 3.
Он автоматически обнаруживает и блокирует пользователей, которые отправляют оскорбительные сообщения, имеют неподобающие биографии или пытаются выдать себя за администраторов.

## 📌 Возможности

-   ✅ Автоматическая блокировка пользователей за:
    -   Запрещённые слова в сообщениях
    -   Запрещённые слова в биографии
    -   Подозрительные имена или юзернеймы (похожие на имена администраторов)
-   🧹 Удаление сообщения, вызвавшего блокировку
-   🔐 Безопасный и легко настраиваемый
-   💡 Лёгкий и простой в установке

## 🚀 Используемые технологии

-   **Python 3.10+**
-   [Aiogram 3](https://docs.aiogram.dev/) — фреймворк для Telegram ботов (асинхронный)
-   [`python-dotenv`](https://pypi.org/project/python-dotenv/) — для конфигурации окружения
-   Стандартные библиотеки: `logging`, `asyncio`, `difflib`, `pathlib`

## 📁 Структура проекта

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

## ⚙️ Установка

### 1. Клонировать репозиторий

```bash
git clone https://github.com/your_username/SilentGuard.git
```

### 2. Установить зависимости

```bash
pip install -r requirements.txt
```

### 3. Создать файл .env

```ini
BOT_TOKEN = your_telegram_bot_token
```

## 🧠 Как это работает

### Когда SilentGuard добавлен в группу Telegram (в качестве администратора), он:

-   Отслеживает новых пользователей и сообщения
-   Если пользователь заходит с подозрительным именем или ником, он блокируется
-   Если пользователь отправляет сообщение с запрещёнными словами, сообщение удаляется, а пользователь блокируется
-   Если в биографии пользователя содержится запрещённый контент, он также блокируется

## ✅ Пример: Файл чёрного списка (data/blacklist.txt)

```perl
# Оскорбительные слова
идиот
тупица

```

## 📌 Настройка администратора

-   Добавьте бота в вашу группу

-   Сделайте его администратором с правами на:

    -   Блокировку пользователей
    -   Удаление сообщений

-   Отредактируйте файл data/blacklist.txt в соответствии с вашими нуждами

## ▶️ Запуск бота

После того как все настроено:

```bash
python bot.py
```

Бот начнёт опрос и будет защищать вашу группу.

## 📋 Возможные улучшения

-   **Команда администратора для перезагрузки чёрного списка во время работы**  
    Позволяет администраторам перезагружать чёрный список без перезапуска бота.

-   **Веб-панель для управления чёрным списком**  
    Простой браузерный интерфейс для просмотра, добавления или удаления слов из чёрного списка.

-   **Поддержка белого списка**  
    Доверенные пользователи будут игнорироваться всеми фильтрами и никогда не будут заблокированы.

-   **Анти-флуд система**  
    Обнаружение и заглушение или блокировка пользователей, которые отправляют слишком много сообщений за короткий промежуток времени.

## 📝 Лицензия

Этот проект с открытым исходным кодом и доступен по лицензии [MIT License](LICENSE).
