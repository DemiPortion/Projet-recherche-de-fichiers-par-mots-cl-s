import json

FAVORITES_FILE = "index/favorites.json"

def add_to_favorites(file_path):
    try:
        with open(FAVORITES_FILE, "r", encoding="utf-8") as f:
            favorites = json.load(f)
    except FileNotFoundError:
        favorites = []

    if file_path not in favorites:
        favorites.append(file_path)

    with open(FAVORITES_FILE, "w", encoding="utf-8") as f:
        json.dump(favorites, f, ensure_ascii=False, indent=4)

def get_favorites():
    try:
        with open(FAVORITES_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def remove_from_favorites(file_path):
    try:
        with open(FAVORITES_FILE, "r", encoding="utf-8") as f:
            favorites = json.load(f)
    except FileNotFoundError:
        favorites = []

    if file_path in favorites:
        favorites.remove(file_path)

    with open(FAVORITES_FILE, "w", encoding="utf-8") as f:
        json.dump(favorites, f, ensure_ascii=False, indent=4)
