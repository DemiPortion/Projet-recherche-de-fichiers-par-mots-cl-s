import tkinter as tk
from tkinter import ttk
from random import randint
import matplotlib.pyplot as plt

def tp_2_1():
    def run_simulation():
        try:
            rolls = int(entry.get())
            if rolls <= 0:
                raise ValueError("Le nombre de lancers doit être positif.")
            
            # Calcul des fréquences
            frequencies = {i: 0 for i in range(1, 7)}
            for _ in range(rolls):
                roll = randint(1, 6)
                frequencies[roll] += 1

            # Mise à jour des résultats
            result_text.set("\n".join([f"Face {face} : {count}" for face, count in frequencies.items()]))
            visualize_frequencies(frequencies)
        except ValueError as e:
            result_text.set(f"Erreur : {e}")

    def visualize_frequencies(frequencies):
        faces = list(frequencies.keys())
        counts = list(frequencies.values())

        plt.figure(figsize=(8, 6))
        plt.bar(faces, counts, color="skyblue", edgecolor="black")
        plt.title("Distribution des lancers de dés", fontsize=16)
        plt.xlabel("Face du dé", fontsize=14)
        plt.ylabel("Fréquence", fontsize=14)
        plt.xticks(faces, fontsize=12)
        plt.yticks(fontsize=12)
        plt.grid(axis="y", linestyle="--", alpha=0.7)
        plt.tight_layout()
        plt.show()

    def close_window():
        window.destroy()

    # Création de la fenêtre principale
    window = tk.Toplevel()
    window.title("TP 2.1 : Simulation de lancers de dés")
    window.geometry("800x600")
    window.configure(bg="#f2f2f2")

    # Création du cadre principal
    frame = ttk.Frame(window, padding=20)
    frame.pack(expand=True)

    # Entrée pour le nombre de lancers
    ttk.Label(frame, text="Nombre de lancers de dés :", font=("Arial", 14)).pack(pady=10)
    entry = ttk.Entry(frame, width=30)
    entry.pack(pady=10)

    # Zone pour afficher les résultats
    result_text = tk.StringVar()
    result_label = ttk.Label(frame, textvariable=result_text, font=("Arial", 12), background="#f2f2f2", anchor="center")
    result_label.pack(pady=20)

    # Boutons d'action
    ttk.Button(frame, text="Simuler", command=run_simulation).pack(pady=10)
    ttk.Button(frame, text="Quitter", command=close_window).pack(pady=10)
