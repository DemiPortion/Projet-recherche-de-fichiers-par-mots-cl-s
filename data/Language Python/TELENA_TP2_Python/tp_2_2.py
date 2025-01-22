import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt

def tp_2_2():
    def calculate_statistics():
        try:
            numbers = list(map(float, entry.get().split()))
            if not numbers:
                raise ValueError("Veuillez entrer au moins une note.")
            if any(n < 0 or n > 20 for n in numbers):
                raise ValueError("Toutes les notes doivent être comprises entre 0 et 20.")

            mean = np.mean(numbers)
            median = np.median(numbers)
            q1 = np.percentile(numbers, 25)
            q3 = np.percentile(numbers, 75)
            iqr = q3 - q1

            result_text.set(
                f"Moyenne: {mean:.2f}\n"
                f"Médiane: {median:.2f}\n"
                f"Q1 (1er quartile): {q1:.2f}\n"
                f"Q3 (3e quartile): {q3:.2f}\n"
                f"IQR (Écart interquartile): {iqr:.2f}"
            )
            visualize_statistics(numbers, mean, median, q1, q3)
        except ValueError as e:
            result_text.set(f"Erreur : {e}")

    def visualize_statistics(numbers, mean, median, q1, q3):
        plt.figure(figsize=(8, 6))
        plt.plot(numbers, [mean] * len(numbers), label="Moyenne", color="blue", linestyle="--")
        plt.plot(numbers, [median] * len(numbers), label="Médiane", color="green", linestyle="-.")
        plt.plot(numbers, [q1] * len(numbers), label="1er Quartile (Q1)", color="orange", linestyle=":")
        plt.plot(numbers, [q3] * len(numbers), label="3e Quartile (Q3)", color="red", linestyle=":")
        plt.scatter(range(len(numbers)), numbers, label="Notes", color="purple", zorder=5)
        plt.title("Graphique des statistiques des notes", fontsize=16)
        plt.xlabel("Index des notes", fontsize=14)
        plt.ylabel("Valeurs", fontsize=14)
        plt.legend(fontsize=12)
        plt.grid(axis="y", linestyle="--", alpha=0.7)
        plt.tight_layout()
        plt.show()

    def close_window():
        window.destroy()

    # Création de la fenêtre principale
    window = tk.Toplevel()
    window.title("TP 2.2 : Calcul des statistiques des notes")
    window.geometry("800x600")
    window.configure(bg="#f2f2f2")

    # Cadre principal
    frame = ttk.Frame(window, padding=20)
    frame.pack(expand=True)

    # Entrée des notes
    ttk.Label(frame, text="Entrez les notes séparées par des espaces (entre 0 et 20) :", font=("Arial", 14)).pack(pady=10)
    entry = ttk.Entry(frame, width=50)
    entry.pack(pady=10)

    # Résultats affichés
    result_text = tk.StringVar()
    ttk.Label(frame, textvariable=result_text, font=("Arial", 12), background="#f2f2f2", anchor="center").pack(pady=20)

    # Boutons d'action
    ttk.Button(frame, text="Calculer", command=calculate_statistics).pack(pady=10)
    ttk.Button(frame, text="Quitter", command=close_window).pack(pady=10)
