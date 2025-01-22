import tkinter as tk
from tkinter import ttk
import subprocess

def launch_script(script_name):
    try:
        subprocess.Popen(["python", script_name])
    except Exception as e:
        print(f"Erreur lors du lancement de {script_name}: {e}")

def main():
    # Création de la fenêtre principale
    window = tk.Tk()
    window.title("Menu Principal TP")
    window.geometry("500x400")
    window.resizable(False, False)

    # Titre
    ttk.Label(window, text="Menu des Travaux Pratiques", font=("Arial", 16, "bold")).pack(pady=20)

    # Boutons pour chaque TP
    scripts = {
        "TP1 : Conversion Température": "tpx_1.py",
        "TP2 : Somme et Produit des Pairs": "tpx_2.py",
        "TP3 : Message d'Accueil": "tpx_3.py",
        "TP4 : Jeu de Calcul Mental": "tpx_4.py",
        "TP5 : Année Bissextile": "tpx_5.py",
        "TP6 : Nombre Parfait": "tpx_6.py",
    }

    # Ajout des boutons dans la fenêtre
    for label, script in scripts.items():
        btn = ttk.Button(
            window, text=label, command=lambda s=script: launch_script(s), width=40
        )
        btn.pack(pady=10)

    ttk.Button(window, text="Quitter", command=window.quit, width=20).pack(pady=20)

    window.mainloop()

if __name__ == "__main__":
    main()
