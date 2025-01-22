import json
import os
from datetime import datetime

def search_in_index(keyword, file_type=None, date_after=None, date_before=None, index_file="index/index.json"):
    with open(index_file, "r", encoding="utf-8") as f:
        index = json.load(f)
    
    results = []
    for entry in index:
        # Filtrer par mot-clé
        if keyword.lower() not in entry["content"].lower():
            continue

        # Filtrer par type de fichier
        if file_type and not entry["file_path"].endswith(file_type):
            continue

        # Filtrer par date de modification
        file_mod_time = os.path.getmtime(entry["file_path"])  # Récupérer l'horodatage
        file_date = datetime.fromtimestamp(file_mod_time)

        # Comparer avec la plage de dates si spécifiée
        if date_after and file_date < datetime.strptime(date_after, "%Y-%m-%d"):
            continue
        if date_before and file_date > datetime.strptime(date_before, "%Y-%m-%d"):
            continue

        results.append(entry["file_path"])
    
    return results
