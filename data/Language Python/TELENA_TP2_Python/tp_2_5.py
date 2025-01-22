import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time

def tp_2_5():
    class Port:
        def __init__(self, nom):
            self.nom = nom
            self.bateaux = []

        def ajouter_bateau(self, bateau):
            self.bateaux.append(bateau)

        def retirer_bateau(self, index):
            if 0 <= index < len(self.bateaux):
                self.bateaux.pop(index)

        def afficher_bateaux(self):
            return [f"Nom: {b.nom}, Longueur: {b.longueur}" for b in self.bateaux]

        def naviguer_tous(self):
            if not self.bateaux:
                messagebox.showerror("Erreur", "Aucun bateau dans le port!")
                return
            messagebox.showinfo("Navigation", "Tous les bateaux sont en train de naviguer!")
            animate_all_boats()

    class Bateau:
        def __init__(self, nom, longueur):
            self.nom = nom
            self.longueur = longueur

        def modifier(self, nouveau_nom, nouvelle_longueur):
            self.nom = nouveau_nom
            self.longueur = nouvelle_longueur

    def add_bateau():
        try:
            bateau = Bateau(entry_bateau_nom.get(), float(entry_bateau_longueur.get()))
            port.ajouter_bateau(bateau)
            refresh_list()
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer des valeurs valides pour le bateau.")

    def remove_bateau():
        selected = listbox.curselection()
        if selected:
            port.retirer_bateau(selected[0])
            refresh_list()

    def modify_bateau():
        selected = listbox.curselection()
        if selected:
            index = selected[0]
            try:
                nouveau_nom = entry_modify_nom.get()
                nouvelle_longueur = float(entry_modify_longueur.get())
                port.bateaux[index].modifier(nouveau_nom, nouvelle_longueur)
                refresh_list()
            except ValueError:
                messagebox.showerror("Erreur", "Veuillez entrer des valeurs valides pour la modification.")
        else:
            messagebox.showerror("Erreur", "Veuillez sélectionner un bateau à modifier!")

    def refresh_list():
        listbox.delete(0, tk.END)
        for info in port.afficher_bateaux():
            listbox.insert(tk.END, info)

    def animate_all_boats():
        def move_boats():
            canvas.delete("all")
            boat_positions = [50 * i + 10 for i in range(len(port.bateaux))]
            boats = [
                canvas.create_rectangle(x, 50, x + 40, 90, fill="blue", outline="black")
                for x in boat_positions
            ]
            labels = [
                canvas.create_text(x + 20, 100, text=b.nom, font=("Arial", 10))
                for x, b in zip(boat_positions, port.bateaux)
            ]

            for _ in range(50):
                for boat in boats:
                    canvas.move(boat, 5, 0)
                for label in labels:
                    canvas.move(label, 5, 0)
                time.sleep(0.05)

        threading.Thread(target=move_boats).start()

    def close_window():
        window.destroy()

    port = Port("Port Principal")

    # Fenêtre principale
    window = tk.Toplevel()
    window.title("TP 2.5 : Port")
    window.geometry("900x600")
    window.configure(bg="#f2f2f2")

    frame = ttk.Frame(window, padding=20)
    frame.pack(side="left", fill="both", expand=True)

    # Entrées pour créer un bateau
    ttk.Label(frame, text="Nom du bateau :", font=("Arial", 14)).grid(row=0, column=0, padx=10, pady=10)
    entry_bateau_nom = ttk.Entry(frame, width=30)
    entry_bateau_nom.grid(row=0, column=1, padx=10, pady=10)

    ttk.Label(frame, text="Longueur du bateau :", font=("Arial", 14)).grid(row=1, column=0, padx=10, pady=10)
    entry_bateau_longueur = ttk.Entry(frame, width=30)
    entry_bateau_longueur.grid(row=1, column=1, padx=10, pady=10)

    ttk.Button(frame, text="Ajouter Bateau", command=add_bateau).grid(row=2, column=0, columnspan=2, pady=20)

    # Liste des bateaux
    ttk.Label(frame, text="Liste des bateaux :", font=("Arial", 14)).grid(row=3, column=0, columnspan=2, pady=10)
    listbox = tk.Listbox(frame, width=50, height=10)
    listbox.grid(row=4, column=0, columnspan=2, pady=10)

    # Modification des bateaux
    ttk.Label(frame, text="Modifier le bateau sélectionné :", font=("Arial", 14)).grid(row=5, column=0, columnspan=2, pady=10)
    ttk.Label(frame, text="Nouveau nom :", font=("Arial", 12)).grid(row=6, column=0, padx=10, pady=10)
    entry_modify_nom = ttk.Entry(frame, width=30)
    entry_modify_nom.grid(row=6, column=1, padx=10, pady=10)

    ttk.Label(frame, text="Nouvelle longueur :", font=("Arial", 12)).grid(row=7, column=0, padx=10, pady=10)
    entry_modify_longueur = ttk.Entry(frame, width=30)
    entry_modify_longueur.grid(row=7, column=1, padx=10, pady=10)

    ttk.Button(frame, text="Modifier", command=modify_bateau).grid(row=8, column=0, columnspan=2, pady=20)
    ttk.Button(frame, text="Retirer Bateau", command=remove_bateau).grid(row=9, column=0, columnspan=2, pady=10)

    ttk.Button(frame, text="Faire naviguer tous les bateaux", command=port.naviguer_tous).grid(row=10, column=0, columnspan=2, pady=20)
    ttk.Button(frame, text="Quitter", command=close_window).grid(row=11, column=0, columnspan=2, pady=20)

    # Canvas pour l'animation
    canvas = tk.Canvas(window, width=600, height=200, bg="white")
    canvas.pack(side="right", fill="both", expand=True)
