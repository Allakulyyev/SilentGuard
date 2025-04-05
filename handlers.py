import logging
from aiogram import Bot, Dispatcher, F, types
from aiogram.enums import ContentType

from utils import load_blacklist
from filters import is_user_suspicious, contains_blacklisted_word


def register_handlers(dp: Dispatcher, bot: Bot):
    """
    Registers all bot handlers. Called from bot.py on startup.
    """
    dp.message.register(on_user_added, F.new_chat_members)
    dp.message.register(on_text_message, F.content_type == ContentType.TEXT)


async def on_user_added(message: types.Message, bot: Bot):
    """
    Triggered when new users join the chat.
    Checks for suspicious names or usernames.
    """
    blacklist = load_blacklist()
    chat_id = message.chat.id
    admins = await bot.get_chat_administrators(chat_id)

    for user in message.new_chat_members:
        if is_user_suspicious(user, admins, blacklist):
            await ban_user(bot, chat_id, user, reason="suspicious name or username (possible admin impersonation)")


async def on_text_message(message: types.Message, bot: Bot):
    """
    Triggered on every text message.
    Checks for blacklisted words in message and user bio.
    """
    blacklist = load_blacklist()
    user = message.from_user
    chat_id = message.chat.id

    if contains_blacklisted_word(message.text, blacklist):
        await ban_user(bot, chat_id, user, reason="use of blacklisted words", message=message)
        return

    try:
        member = await bot.get_chat_member(chat_id, user.id)
        bio = getattr(member, "bio", None)
        if bio and contains_blacklisted_word(bio, blacklist):
            await ban_user(bot, chat_id, user, reason="blacklisted words in bio", message=message)
    except Exception as e:
        logging.warning(f"Failed to fetch bio for user {user.id}: {e}")


async def ban_user(bot: Bot, chat_id: int, user: types.User, reason: str, message: types.Message = None):
    """
    Bans a user and deletes the original message (if provided).
    Sends a message to the chat with the reason.
    """
    try:
        await bot.ban_chat_member(chat_id, user.id)

        # Always delete the message if it's given
        if message:
            try:
                await bot.delete_message(chat_id, message.message_id)
            except Exception as e:
                logging.warning(f"Failed to delete message from {user.full_name}: {e}")

        await bot.send_message(chat_id, f"<b>{user.full_name}</b> was banned for {reason}.")
    except Exception as e:
        logging.error(f"Failed to ban {user.full_name} (@{user.username}): {e}")
