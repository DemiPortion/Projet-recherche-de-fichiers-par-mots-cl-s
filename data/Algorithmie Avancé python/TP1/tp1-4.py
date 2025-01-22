import tkinter as tk
from tkinter import messagebox
import random

# Fonction pour générer la question et vérifier la réponse
def poser_question():
    # Récupérer le type d'opération choisi
    operation = var_operation.get()

    # Générer deux nombres aléatoires
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    # Poser la question en fonction de l'opération choisie
    if operation == "addition":
        correct_answer = num1 + num2
        question = f"Combien fait {num1} + {num2} ?"
    elif operation == "soustraction":
        correct_answer = num1 - num2
        question = f"Combien fait {num1} - {num2} ?"
    elif operation == "multiplication":
        correct_answer = num1 * num2
        question = f"Combien fait {num1} x {num2} ?"
    elif operation == "division":
        # Eviter la division par zéro
        num2 = random.randint(1, 10)
        while num1 % num2 != 0:  # S'assurer que num1 est divisible par num2
            num2 = random.randint(1, 10)
        correct_answer = num1 // num2
        question = f"Combien fait {num1} ÷ {num2} ?"

    # Afficher la question dans l'interface
    label_question.config(text=question)

    # Fonction pour vérifier la réponse de l'utilisateur
    def verifier_reponse():
        try:
            user_answer = int(entry_reponse.get())  # Récupérer la réponse de l'utilisateur
            if user_answer == correct_answer:
                messagebox.showinfo("Réponse", "Correct !")
            else:
                messagebox.showerror("Réponse", f"Incorrect. La bonne réponse est {correct_answer}.")
            entry_reponse.delete(0, tk.END)  # Réinitialiser le champ de saisie
            poser_question()  # Reposer une nouvelle question

        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer un nombre valide.")

    # Ajouter un bouton pour vérifier la réponse
    button_verifier.config(command=verifier_reponse)

# Créer la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Calcul Mental")
fenetre.geometry("400x300")
fenetre.configure(bg="#f8f9fa")

# Styles
font_title = ("Arial", 18, "bold")
font_label = ("Arial", 14)
font_button = ("Arial", 12, "bold")

# Widgets de l'interface
label_title = tk.Label(fenetre, text="Calcul Mental", font=font_title, bg="#f8f9fa", fg="#333")
label_title.pack(pady=10)

label_instruction = tk.Label(fenetre, text="Choisissez le type d'opération :", font=font_label, bg="#f8f9fa", fg="#555")
label_instruction.pack(pady=5)

# Variable pour sélectionner l'opération
var_operation = tk.StringVar(value="addition")

# Créer les boutons radio pour les opérations
radio_addition = tk.Radiobutton(fenetre, text="Addition", variable=var_operation, value="addition", font=font_label, bg="#f8f9fa", fg="#555")
radio_addition.pack(pady=5)

radio_soustraction = tk.Radiobutton(fenetre, text="Soustraction", variable=var_operation, value="soustraction", font=font_label, bg="#f8f9fa", fg="#555")
radio_soustraction.pack(pady=5)

radio_multiplication = tk.Radiobutton(fenetre, text="Multiplication", variable=var_operation, value="multiplication", font=font_label, bg="#f8f9fa", fg="#555")
radio_multiplication.pack(pady=5)

radio_division = tk.Radiobutton(fenetre, text="Division", variable=var_operation, value="division", font=font_label, bg="#f8f9fa", fg="#555")
radio_division.pack(pady=5)

# Bouton pour générer la question après le choix de l'opération
button_generer = tk.Button(fenetre, text="Générer la question", command=poser_question, font=font_button, bg="#007bff", fg="white", activebackground="#0056b3", relief="flat", cursor="hand2")
button_generer.pack(pady=10, ipadx=10, ipady=5)

# Label pour afficher la question
label_question = tk.Label(fenetre, text="", font=("Arial", 16), bg="#f8f9fa", fg="#333")
label_question.pack(pady=20)

# Champ pour entrer la réponse
entry_reponse = tk.Entry(fenetre, font=("Arial", 14), justify="center", bd=2, relief="solid")
entry_reponse.pack(ipady=5, pady=5)

# Bouton pour vérifier la réponse
button_verifier = tk.Button(fenetre, text="Vérifier la réponse", font=font_button, bg="#28a745", fg="white", activebackground="#218838", relief="flat", cursor="hand2")
button_verifier.pack(pady=20, ipadx=10, ipady=5)

# Lancer la boucle principale
fenetre.mainloop()
