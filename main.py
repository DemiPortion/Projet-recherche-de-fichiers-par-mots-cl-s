import os
import platform
import subprocess
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from datetime import datetime
from scanner import scan_folder
from indexer import create_index
from search import search_in_index
from history import save_to_history, get_history
from favorites import add_to_favorites, remove_from_favorites, get_favorites

app = Flask(__name__)
app.secret_key = "une_cle_secrete_au_hasard"
FOLDER_PATH = "data"

# Filtre pour formater les dates
@app.template_filter('format_datetime')
def format_datetime(value):
    return datetime.fromtimestamp(value).strftime('%Y-%m-%d %H:%M:%S')

@app.route('/')
def home():
    favorites = get_favorites()
    history = get_history()
    return render_template('index.html', favorites=favorites, history=history)

@app.route('/search', methods=['POST'])
def search():
    keyword = request.form.get('keyword')
    file_type = request.form.get('file_type')
    date_after = request.form.get('date_after')
    date_before = request.form.get('date_before')

    # Sauvegarder la recherche dans l'historique
    save_to_history(keyword, file_type, date_after)

    files = scan_folder(FOLDER_PATH)
    create_index(files)
    raw_results = search_in_index(keyword, file_type, date_after, date_before)

    # Préparer les résultats
    results = []
    for file_path in raw_results:
        file_mod_time = os.path.getmtime(file_path)
        file_info = {
            "path": file_path,
            "type": file_path.split('.')[-1],
            "last_modified": file_mod_time,
        }
        results.append(file_info)

    # Stocker les résultats dans la session
    session['results'] = results
    session['keyword'] = keyword

    return render_template('results.html', keyword=keyword, results=results)

@app.route('/open', methods=['POST'])
def open_file():
    file_path = request.form.get('file_path')

    try:
        if platform.system() == "Windows":
            os.startfile(file_path)
        elif platform.system() == "Darwin":  # macOS
            subprocess.run(["open", file_path], check=True)
        else:  # Linux
            subprocess.run(["xdg-open", file_path], check=True)
    except Exception as e:
        return f"Erreur : Impossible d'ouvrir le fichier. {e}", 500

    return redirect(url_for('home'))

@app.route('/favorites')
def favorites():
    favorites = get_favorites()
    return render_template('favorites.html', favorites=favorites)

@app.route('/add_favorite', methods=['POST'])
def add_favorite():
    file_path = request.form.get('file_path')
    add_to_favorites(file_path)
    return redirect(url_for('favorites'))

@app.route('/remove_favorite', methods=['POST'])
def remove_favorite():
    file_path = request.form.get('file_path')
    remove_from_favorites(file_path)
    return redirect(url_for('favorites'))

@app.route('/delete_favorites', methods=['POST'])
def delete_favorites():
    data = request.get_json()
    files_to_remove = data.get('files', [])
    for file_path in files_to_remove:
        remove_from_favorites(file_path)
    return jsonify({"status": "success"})


@app.route('/toggle_favorite', methods=['POST'])
def toggle_favorite():
    file_path = request.json.get('file_path')
    favorites = get_favorites()

    if file_path in favorites:
        remove_from_favorites(file_path)
        return jsonify({"status": "removed", "file": file_path})
    else:
        add_to_favorites(file_path)
        return jsonify({"status": "added", "file": file_path})

if __name__ == "__main__":
    app.run(debug=True)


