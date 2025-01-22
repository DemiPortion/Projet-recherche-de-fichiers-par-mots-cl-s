import json

HISTORY_FILE = "index/history.json"
HISTORY_LIMIT = 10  # Limite du nombre d’entrées dans l’historique


def save_to_history(keyword, file_type=None, date_after=None, date_before=None):
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            history = json.load(f)
    except FileNotFoundError:
        history = []

    # Ajouter une nouvelle recherche en haut de la liste
    history.insert(0, {
        "keyword": keyword,
        "file_type": file_type,
        "date_after": date_after,
        "date_before": date_before
    })

    # Supprimer les entrées les plus anciennes si la limite est dépassée
    history = history[:HISTORY_LIMIT]

    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=4)


def get_history():
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
