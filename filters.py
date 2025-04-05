import difflib


def contains_blacklisted_word(text: str, blacklist: set[str]) -> bool:
    """
    Returns True if any word from the blacklist is found in the text.
    """
    if not text:
        return False

    text = text.lower()
    return any(bad_word in text for bad_word in blacklist)


def similarity(a: str, b: str) -> float:
    """
    Returns the similarity ratio between two strings (0.0 to 1.0).
    """
    return difflib.SequenceMatcher(None, a, b).ratio()


def get_user_identifiers(user) -> tuple[str, str]:
    """
    Returns user's full name and username in lowercase.
    """
    full_name = f"{user.first_name or ''} {user.last_name or ''}".strip().lower()
    username = (user.username or "").lower()
    return full_name, username


def is_name_like_admin(user_name: str, admin_name: str) -> bool:
    """
    Returns True if names match or are over 80% similar.
    """
    return (
        user_name == admin_name or
        similarity(user_name, admin_name) > 0.8
    )


def is_user_suspicious(user, admins: list, blacklist: set[str]) -> bool:
    """
    Checks if a user is suspicious:
    - Contains blacklisted words in name or username
    - Tries to impersonate an admin
    """
    full_name, username = get_user_identifiers(user)

    if contains_blacklisted_word(full_name, blacklist) or contains_blacklisted_word(username, blacklist):
        return True

    for admin in admins:
        admin_full, admin_user = get_user_identifiers(admin.user)

        if (
            is_name_like_admin(full_name, admin_full) or
            is_name_like_admin(username, admin_user) or
            is_name_like_admin(full_name, admin_user) or
            is_name_like_admin(username, admin_full)
        ):
            return True

    return False
