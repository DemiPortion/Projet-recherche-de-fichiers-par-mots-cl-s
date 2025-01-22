import tkinter as tk
from tkinter import messagebox
import random

# Fonction pour générer un message d'accueil personnalisé
def accueil_personnalise():
    try:
        # Récupérer la liste de noms entrée par l'utilisateur
        noms = entry_noms.get()
        # Convertir la chaîne en liste en séparant par les virgules et en enlevant les espaces
        noms_liste = [nom.strip() for nom in noms.split(",")]
        
        # Liste des messages d'accueil standard
        messages = ["Bonjour", "Salut", "Bienvenue"]
        
        # Créer les messages d'accueil pour chaque nom
        messages_accueil = []
        for nom in noms_liste:
            message = random.choice(messages)  # Choisir un message d'accueil au hasard
            messages_accueil.append(f"{message}, {nom}!")  # Personnaliser le message

        # Afficher les messages dans une boîte de dialogue
        messagebox.showinfo("Messages d'accueil", "\n".join(messages_accueil))
        
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer une liste de noms valide.")

# Créer la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Messages d'Accueil Personnalisés")
fenetre.geometry("400x300")
fenetre.configure(bg="#f8f9fa")

# Styles
font_title = ("Arial", 18, "bold")
font_label = ("Arial", 14)
font_button = ("Arial", 12, "bold")

# Widgets de l'interface
label_title = tk.Label(fenetre, text="Messages d'Accueil Personnalisés", font=font_title, bg="#f8f9fa", fg="#333")
label_title.pack(pady=10)

label_instruction = tk.Label(fenetre, text="Entrez une liste de noms (séparés par des virgules) :", font=font_label, bg="#f8f9fa", fg="#555")
label_instruction.pack(pady=5)

entry_noms = tk.Entry(fenetre, font=("Arial", 12), justify="center", bd=2, relief="solid")
entry_noms.pack(ipady=5, pady=5)

button_accueil = tk.Button(fenetre, text="Générer les messages", command=accueil_personnalise, font=font_button, bg="#007bff", fg="white", activebackground="#0056b3", relief="flat", cursor="hand2")
button_accueil.pack(pady=20, ipadx=10, ipady=5)

# Lancer la boucle principale
fenetre.mainloop()
