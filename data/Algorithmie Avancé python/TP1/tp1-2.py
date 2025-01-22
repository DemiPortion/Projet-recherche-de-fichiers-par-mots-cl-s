import tkinter as tk
from tkinter import messagebox

# Fonction pour calculer la somme et le produit des nombres pairs
def calculer():
    try:
        N = int(entry_N.get())
        if N <= 0:
            messagebox.showerror("Erreur", "Veuillez entrer un entier positif.")
            return
        
        # Liste des nombres pairs jusqu'à N
        nombres_pairs = [i for i in range(2, N+1, 2)]
        
        # Calcul de la somme et du produit
        somme = sum(nombres_pairs)
        produit = 1
        for nombre in nombres_pairs:
            produit *= nombre
        
        # Affichage du résultat sous les 2 formats demandés
        somme_str = " + ".join(map(str, nombres_pairs)) + f" = {somme}"
        somme_reverse_str = f"{somme} = " + " + ".join(map(str, nombres_pairs))
        
        produit_str = " * ".join(map(str, nombres_pairs)) + f" = {produit}"
        produit_reverse_str = f"{produit} = " + " * ".join(map(str, nombres_pairs))

        # Affichage des résultats dans une boîte de dialogue
        messagebox.showinfo("Résultats", f"{somme_str}\n{somme_reverse_str}\n\n{produit_str}\n{produit_reverse_str}")
        
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer un nombre entier valide.")

# Fonction pour redémarrer le programme
def recommencer():
    entry_N.delete(0, tk.END)

# Créer la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Calcul de Somme et Produit des Nombres Pairs")
fenetre.geometry("400x300")
fenetre.configure(bg="#f8f9fa")

# Styles
font_title = ("Arial", 18, "bold")
font_label = ("Arial", 14)
font_button = ("Arial", 12, "bold")

# Widgets de l'interface
label_title = tk.Label(fenetre, text="Somme et Produit des Nombres Pairs", font=font_title, bg="#f8f9fa", fg="#333")
label_title.pack(pady=10)

label_instruction = tk.Label(fenetre, text="Entrez un entier positif N :", font=font_label, bg="#f8f9fa", fg="#555")
label_instruction.pack(pady=5)

entry_N = tk.Entry(fenetre, font=("Arial", 12), justify="center", bd=2, relief="solid")
entry_N.pack(ipady=5, pady=5)

button_calculer = tk.Button(fenetre, text="Calculer", command=calculer, font=font_button, bg="#007bff", fg="white", activebackground="#0056b3", relief="flat", cursor="hand2")
button_calculer.pack(pady=20, ipadx=10, ipady=5)

# Ajouter un bouton pour recommencer
button_recommencer = tk.Button(fenetre, text="Recommencer", command=recommencer, font=font_button, bg="#dc3545", fg="white", activebackground="#c82333", relief="flat", cursor="hand2")
button_recommencer.pack(pady=10, ipadx=10, ipady=5)

# Lancer la boucle principale
fenetre.mainloop()
