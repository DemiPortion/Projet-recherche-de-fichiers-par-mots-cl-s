import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np

def tp_2_3():
    def calculate_statistics():
        try:
            prices = list(map(float, entry.get().split()))
            if not prices:
                raise ValueError("Veuillez entrer au moins un prix.")
            if any(p < 0 for p in prices):
                raise ValueError("Les prix doivent être positifs.")

            mean = np.mean(prices)
            variance = np.var(prices)
            std_dev = np.std(prices)

            result_text.set(
                f"Moyenne: {mean:.2f}\n"
                f"Variance: {variance:.2f}\n"
                f"Écart-type: {std_dev:.2f}"
            )
            visualize_statistics(prices, mean, std_dev)
        except ValueError as e:
            result_text.set(f"Erreur : {e}")

    def visualize_statistics(prices, mean, std_dev):
        x = range(1, len(prices) + 1)
        plt.figure(figsize=(8, 6))
        plt.bar(x, prices, color="skyblue", edgecolor="black", label="Prix")
        plt.axhline(y=mean, color="blue", linestyle="--", label=f"Moyenne ({mean:.2f})")
        plt.fill_between(x, mean - std_dev, mean + std_dev, color="orange", alpha=0.3, label=f"± Écart-type ({std_dev:.2f})")
        plt.title("Visualisation des prix et statistiques", fontsize=16)
        plt.xlabel("Index des prix", fontsize=14)
        plt.ylabel("Prix", fontsize=14)
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        plt.legend(fontsize=12)
        plt.grid(axis="y", linestyle="--", alpha=0.7)
        plt.tight_layout()
        plt.show()

    def close_window():
        window.destroy()

    # Création de la fenêtre principale
    window = tk.Toplevel()
    window.title("TP 2.3 : Calcul de la Variance et Écart-type")
    window.geometry("800x600")
    window.configure(bg="#f2f2f2")

    # Cadre principal
    frame = ttk.Frame(window, padding=20)
    frame.pack(expand=True)

    # Entrée des prix
    ttk.Label(frame, text="Entrez les prix séparés par des espaces (positifs) :", font=("Arial", 14)).pack(pady=10)
    entry = ttk.Entry(frame, width=50)
    entry.pack(pady=10)

    # Résultats affichés
    result_text = tk.StringVar()
    ttk.Label(frame, textvariable=result_text, font=("Arial", 12), background="#f2f2f2", anchor="center").pack(pady=20)

    # Boutons d'action
    ttk.Button(frame, text="Calculer", command=calculate_statistics).pack(pady=10)
    ttk.Button(frame, text="Quitter", command=close_window).pack(pady=10)
