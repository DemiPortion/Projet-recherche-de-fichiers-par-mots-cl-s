import tkinter as tk
from tkinter import ttk, messagebox
import random
import time

def launch_tpx_4():
    def start_game():
        """Démarre le jeu en générant une question aléatoire."""
        nonlocal score, start_time
        score = 0
        start_time = time.time()
        next_question()

    def next_question():
        """Génère une nouvelle question et met à jour l'affichage."""
        nonlocal correct_answer, question_start_time
        operation = operation_var.get()
        if not operation:
            messagebox.showwarning("Erreur", "Veuillez choisir une opération.")
            return

        # Génération des nombres aléatoires
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        question_start_time = time.time()

        if operation == "Addition":
            lbl_question.config(text=f"Combien fait {num1} + {num2} ?")
            correct_answer = num1 + num2
        elif operation == "Soustraction":
            lbl_question.config(text=f"Combien fait {num1} - {num2} ?")
            correct_answer = num1 - num2
        elif operation == "Multiplication":
            lbl_question.config(text=f"Combien fait {num1} × {num2} ?")
            correct_answer = num1 * num2
        elif operation == "Division":
            num1, num2 = max(num1, num2), min(num1, num2)
            lbl_question.config(text=f"Combien fait {num1} ÷ {num2} ?")
            correct_answer = round(num1 / num2, 2)

        entry_answer.delete(0, tk.END)

    def check_answer():
        """Vérifie la réponse de l'utilisateur."""
        nonlocal score
        try:
            user_answer = float(entry_answer.get())
            question_time = round(time.time() - question_start_time, 2)

            if abs(user_answer - correct_answer) < 0.01:
                score += 1
                messagebox.showinfo("Bravo", f"Bonne réponse ! Temps : {question_time} secondes")
            else:
                messagebox.showerror("Faux", f"Mauvaise réponse. La bonne réponse était {correct_answer}.")

            next_question()
        except ValueError:
            messagebox.showwarning("Erreur", "Veuillez entrer un nombre valide.")

    def end_game():
        """Termine le jeu et affiche le score final."""
        total_time = round(time.time() - start_time, 2)
        messagebox.showinfo("Fin du jeu", f"Votre score : {score}\nTemps total : {total_time} secondes")
        window.destroy()

    # Initialisation des variables
    correct_answer = 0
    score = 0
    start_time = 0
    question_start_time = 0

    # Création de la fenêtre principale
    window = tk.Tk()
    window.title("Jeu de Calcul Mental")
    window.geometry("600x500")
    window.resizable(False, False)

    # Titre
    ttk.Label(window, text="TP4 : Jeu de Calcul Mental", font=("Arial", 16, "bold")).pack(pady=10)
    ttk.Label(window, text="Choisissez un type d'opération et répondez aux questions.", font=("Arial", 12)).pack(pady=10)

    # Choix de l'opération
    operation_var = tk.StringVar()
    operations = ["Addition", "Soustraction", "Multiplication", "Division"]
    ttk.Label(window, text="Choisissez une opération :", font=("Arial", 12)).pack(pady=5)
    for op in operations:
        ttk.Radiobutton(window, text=op, variable=operation_var, value=op).pack()

    # Zone d'affichage de la question
    lbl_question = ttk.Label(window, text="", font=("Arial", 14, "bold"))
    lbl_question.pack(pady=20)

    # Entrée pour la réponse
    ttk.Label(window, text="Entrez votre réponse :", font=("Arial", 12)).pack(pady=5)
    entry_answer = ttk.Entry(window, font=("Arial", 12), width=20, justify="center")
    entry_answer.pack(pady=5)

    # Boutons de contrôle
    btn_submit = ttk.Button(window, text="Soumettre", command=check_answer)
    btn_submit.pack(pady=10)

    btn_start = ttk.Button(window, text="Commencer", command=start_game)
    btn_start.pack(pady=10)

    btn_quit = ttk.Button(window, text="Terminer le jeu", command=end_game)
    btn_quit.pack(pady=20)

    window.mainloop()

if __name__ == "__main__":
    launch_tpx_4()
