import tkinter as tk
from tkinter import ttk
import random

def launch_tpx_3():
    def generate_greetings():
        names = entry_names.get().split(",")
        greetings = ["Bonjour", "Salut", "Bienvenue"]
        emoji = emoji_var.get()

        if not names or names == [""]:
            lbl_result.config(text="Veuillez entrer au moins un nom.", foreground="red")
            return

        result = ""
        for name in names:
            name = name.strip()
            if name:
                greeting = random.choice(greetings)
                result += f"{greeting}, {name}! {emoji}\n"

        lbl_result.config(text=result, foreground="black")

    def reset():
        entry_names.delete(0, tk.END)
        lbl_result.config(text="")

    window = tk.Tk()
    window.title("Messages d'Accueil Personnalisés")
    window.geometry("600x500")
    window.resizable(False, False)

    # Titre principal
    ttk.Label(window, text="TP3 : Messages d'Accueil Personnalisés", font=("Arial", 16, "bold")).pack(pady=10)

    # Zone d'entrée pour les noms
    ttk.Label(window, text="Entrez une liste de noms (séparés par des virgules) :", font=("Arial", 12)).pack(pady=10)
    entry_names = ttk.Entry(window, font=("Arial", 12), width=50)
    entry_names.pack(pady=5)

    # Choix des emojis
    ttk.Label(window, text="Choisissez un emoji :", font=("Arial", 12)).pack(pady=10)
    emoji_var = tk.StringVar()
    emojis = ["😊", "😎", "🥳", "🎉", "👋", "✨"]
    emoji_menu = ttk.Combobox(window, textvariable=emoji_var, values=emojis, state="readonly", font=("Arial", 12), width=10)
    emoji_menu.current(0)
    emoji_menu.pack(pady=5)

    # Bouton de génération
    btn_generate = ttk.Button(window, text="Générer les Messages", command=generate_greetings)
    btn_generate.pack(pady=10)

    # Zone d'affichage des résultats
    lbl_result = ttk.Label(window, text="", font=("Arial", 12), justify="left", anchor="center", wraplength=550)
    lbl_result.pack(pady=20)

    # Boutons d'options
    btn_reset = ttk.Button(window, text="Réinitialiser", command=reset)
    btn_reset.pack(pady=10)

    btn_close = ttk.Button(window, text="Fermer", command=window.destroy)
    btn_close.pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    launch_tpx_3()
