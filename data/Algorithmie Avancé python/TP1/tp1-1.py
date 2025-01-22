import tkinter as tk
from tkinter import messagebox

# Fonction pour convertir la température
def convertir_temperature():
    try:
        temperature = float(entry_temperature.get())
        conversion = var_conversion.get()
        
        if conversion == "C_to_F":
            resultat = (temperature * 9/5) + 32
            message = f"{temperature:.2f} °C → {resultat:.2f} °F"
        elif conversion == "F_to_C":
            resultat = (temperature - 32) * 5/9
            message = f"{temperature:.2f} °F → {resultat:.2f} °C"
        else:
            message = "Sélectionnez un type de conversion."
        
        # Afficher le résultat dans une boîte de dialogue
        messagebox.showinfo("Résultat", message)
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer une température valide.")

# Fonction pour fermer la fenêtre
def fermer():
    fenetre.destroy()

# Créer la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Convertisseur de Température")
fenetre.geometry("400x300")
fenetre.configure(bg="#f8f9fa")  # Couleur de fond douce

# Styles
font_title = ("Arial", 18, "bold")
font_label = ("Arial", 14)
font_button = ("Arial", 12, "bold")

# Widgets de l'interface
label_title = tk.Label(fenetre, text="Convertisseur de Température", font=font_title, bg="#f8f9fa", fg="#333")
label_title.pack(pady=10)

label_instruction = tk.Label(fenetre, text="Entrez une température :", font=font_label, bg="#f8f9fa", fg="#555")
label_instruction.pack(pady=5)

entry_temperature = tk.Entry(fenetre, font=("Arial", 12), justify="center", bd=2, relief="solid")
entry_temperature.pack(ipady=5, pady=5)

var_conversion = tk.StringVar(value="C_to_F")

radio_c_to_f = tk.Radiobutton(fenetre, text="Celsius à Fahrenheit", variable=var_conversion, value="C_to_F", font=font_label, bg="#f8f9fa", fg="#555", activebackground="#e6f4ff", selectcolor="#e6f4ff")
radio_c_to_f.pack(pady=5)

radio_f_to_c = tk.Radiobutton(fenetre, text="Fahrenheit à Celsius", variable=var_conversion, value="F_to_C", font=font_label, bg="#f8f9fa", fg="#555", activebackground="#e6f4ff", selectcolor="#e6f4ff")
radio_f_to_c.pack(pady=5)

button_convertir = tk.Button(fenetre, text="Convertir", command=convertir_temperature, font=font_button, bg="#007bff", fg="white", activebackground="#0056b3", relief="flat", cursor="hand2")
button_convertir.pack(pady=20, ipadx=10, ipady=5)

# Ajouter le bouton Fermer
button_fermer = tk.Button(fenetre, text="Fermer", command=fermer, font=font_button, bg="#dc3545", fg="white", activebackground="#c82333", relief="flat", cursor="hand2")
button_fermer.pack(pady=10, ipadx=10, ipady=5)

# Lancer la boucle principale
fenetre.mainloop()
