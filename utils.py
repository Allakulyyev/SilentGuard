from pathlib import Path

# Path to the blacklist file: <this_folder>/data/blacklist.txt
BLACKLIST_PATH = Path(__file__).resolve().parent / "data" / "blacklist.txt"


def load_blacklist(file_path: Path = BLACKLIST_PATH) -> set[str]:
    """
    Loads blacklist words from a file.
    Returns a set of lowercase words, skipping empty lines and comments.
    """
    if not file_path.exists():
        return set()

    with file_path.open(encoding="utf-8") as file:
        return {
            line.strip().lower()
            for line in file
            if line.strip() and not line.strip().startswith("#")
        }
