import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time

def tp_2_4():
    class Bateau:
        def __init__(self, nom, longueur, capacite_max):
            self.nom = nom
            self.longueur = longueur
            self.capacite_max = capacite_max
            self.passagers_actuels = 0

        def ajouter_passagers(self, n):
            if self.passagers_actuels + n <= self.capacite_max:
                self.passagers_actuels += n
            else:
                messagebox.showerror("Erreur", "Capacité maximale dépassée!")

        def retirer_passagers(self, n):
            if self.passagers_actuels >= n:
                self.passagers_actuels -= n
            else:
                messagebox.showerror("Erreur", "Nombre de passagers insuffisant!")

        def afficher_informations(self):
            return f"Nom: {self.nom}, Longueur: {self.longueur}, Capacité max: {self.capacite_max}, Passagers: {self.passagers_actuels}"

        def naviguer(self):
            messagebox.showinfo("Navigation", f"Le bateau '{self.nom}' est en train de naviguer!")

    def create_bateau():
        try:
            bateau = Bateau(entry_nom.get(), float(entry_longueur.get()), int(entry_capacite.get()))
            bateaux.append(bateau)
            refresh_bateau_list()
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer des valeurs valides pour le bateau.")

    def refresh_bateau_list():
        listbox.delete(0, tk.END)
        for bateau in bateaux:
            listbox.insert(tk.END, bateau.afficher_informations())

    def start_navigation():
        selected = listbox.curselection()
        if selected:
            index = selected[0]
            bateaux[index].naviguer()
            animate_boat(bateaux[index].nom)
        else:
            messagebox.showerror("Erreur", "Veuillez sélectionner un bateau pour naviguer.")

    def animate_boat(name):
        def move_boat():
            for i in range(50):
                canvas.move(boat, 5, 0)
                time.sleep(0.05)
            canvas.itemconfig(boat_text, text=f"Le bateau '{name}' flotte!")
            time.sleep(1)
            canvas.delete(boat)

        canvas.delete("all")
        boat = canvas.create_rectangle(10, 90, 100, 150, fill="blue", outline="black")
        canvas.create_text(55, 170, text="Bateau", font=("Arial", 10), fill="black")
        boat_text = canvas.create_text(400, 50, text="", font=("Arial", 14))
        threading.Thread(target=move_boat).start()

    def close_window():
        window.destroy()

    bateaux = []

    # Fenêtre principale
    window = tk.Toplevel()
    window.title("TP 2.4 : Gestion des Bateaux")
    window.geometry("800x600")
    window.configure(bg="#f2f2f2")

    frame = ttk.Frame(window, padding=20)
    frame.pack(side="left", fill="both", expand=True)

    # Entrées pour créer un bateau
    ttk.Label(frame, text="Nom du bateau :", font=("Arial", 14)).pack(pady=10)
    entry_nom = ttk.Entry(frame, width=30)
    entry_nom.pack(pady=10)

    ttk.Label(frame, text="Longueur (mètres) :", font=("Arial", 14)).pack(pady=10)
    entry_longueur = ttk.Entry(frame, width=30)
    entry_longueur.pack(pady=10)

    ttk.Label(frame, text="Capacité maximale :", font=("Arial", 14)).pack(pady=10)
    entry_capacite = ttk.Entry(frame, width=30)
    entry_capacite.pack(pady=10)

    ttk.Button(frame, text="Créer", command=create_bateau).pack(pady=10)

    # Liste des bateaux
    ttk.Label(frame, text="Liste des bateaux :", font=("Arial", 14)).pack(pady=10)
    listbox = tk.Listbox(frame, width=50, height=10)
    listbox.pack(pady=10)

    # Boutons pour naviguer et quitter
    ttk.Button(frame, text="Naviguer", command=start_navigation).pack(pady=10)
    ttk.Button(frame, text="Quitter", command=close_window).pack(pady=20)

    # Canvas pour l'animation
    canvas = tk.Canvas(window, width=600, height=200, bg="white")
    canvas.pack(side="right", fill="both", expand=True)
