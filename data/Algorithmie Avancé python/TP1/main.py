import tkinter as tk
import subprocess  # Pour ouvrir un autre fichier Python

# Fonction pour ouvrir TP 1.1
def open_tp1_1():
    subprocess.run(["python", "tp1-1.py"])

# Fonction pour ouvrir TP 1.2 (tu peux personnaliser cette fonction pour ouvrir d'autres TP)
def open_tp1_2():
    subprocess.run(["python", "tp1-2.py"])

def open_tp1_3():
    subprocess.run(["python", "tp1-3.py"])

def open_tp1_4():
    subprocess.run(["python", "tp1-4.py"])

# Fonction pour fermer la fenêtre principale
def fermer():
    fenetre.destroy()

# Créer la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Menu Principal")
fenetre.geometry("400x300")
fenetre.configure(bg="#f8f9fa")

# Styles pour les boutons
font_button = ("Arial", 14, "bold")

# Ajouter des boutons pour chaque TP
button_tp1_1 = tk.Button(fenetre, text="TP 1.1 - Convertisseur de Température", command=open_tp1_1, font=font_button, bg="#007bff", fg="white", activebackground="#0056b3", relief="flat", cursor="hand2")
button_tp1_1.pack(pady=10, ipadx=10, ipady=5)

button_tp1_2 = tk.Button(fenetre, text="TP 1.2 - Nombres premiers", command=open_tp1_2, font=font_button, bg="#007bff", fg="white", activebackground="#0056b3", relief="flat", cursor="hand2")
button_tp1_2.pack(pady=10, ipadx=10, ipady=5)

button_tp1_3 = tk.Button(fenetre, text="TP 1.3 - Messsage d'accueil", command=open_tp1_3, font=font_button, bg="#007bff", fg="white", activebackground="#0056b3", relief="flat", cursor="hand2")
button_tp1_3.pack(pady=10, ipadx=10, ipady=5)

button_tp1_4 = tk.Button(fenetre, text="TP 1.4 - Question calculs mentaux", command=open_tp1_4, font=font_button, bg="#007bff", fg="white", activebackground="#0056b3", relief="flat", cursor="hand2")
button_tp1_4.pack(pady=10, ipadx=10, ipady=5)

# Ajouter un bouton Fermer
button_fermer = tk.Button(fenetre, text="Fermer", command=fermer, font=font_button, bg="#dc3545", fg="white", activebackground="#c82333", relief="flat", cursor="hand2")
button_fermer.pack(pady=20, ipadx=10, ipady=5)

# Lancer la boucle principale
fenetre.mainloop()
