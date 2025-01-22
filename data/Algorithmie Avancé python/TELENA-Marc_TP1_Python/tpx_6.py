import tkinter as tk
from tkinter import ttk, messagebox

def launch_tpx_6():
    def is_perfect_number(number):
        """Vérifie si un nombre est parfait."""
        divisors = [i for i in range(1, number) if number % i == 0]
        return sum(divisors) == number

    def check_number():
        """Vérifie si le nombre entré est parfait et met à jour le score et l'historique."""
        nonlocal score
        try:
            number = int(entry_number.get())
            if number <= 0:
                raise ValueError("Le nombre doit être positif.")

            if is_perfect_number(number):
                result_text = f"{number} est un nombre parfait."
                score += 1
                lbl_score.config(text=f"Score : {score}")
            else:
                result_text = f"{number} n'est pas un nombre parfait."

            # Mettre à jour l'historique
            history_list.insert(tk.END, result_text)
            lbl_result.config(text=result_text, foreground="green" if "parfait" in result_text else "red")

        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer un nombre entier positif valide.")

    def reset():
        """Réinitialise l'interface et le score."""
        nonlocal score
        score = 0
        lbl_score.config(text=f"Score : {score}")
        history_list.delete(0, tk.END)
        lbl_result.config(text="")
        entry_number.delete(0, tk.END)

    window = tk.Tk()
    window.title("Vérification des Nombres Parfaits")
    window.geometry("700x600")
    window.resizable(False, False)

    # Initialisation du score
    score = 0

    # Titre principal
    ttk.Label(window, text="TP6 : Vérification des Nombres Parfaits", font=("Arial", 16, "bold")).pack(pady=10)

    # Zone d'entrée
    ttk.Label(window, text="Entrez un nombre entier positif :", font=("Arial", 12)).pack(pady=10)
    entry_number = ttk.Entry(window, font=("Arial", 12), width=20, justify="center")
    entry_number.pack(pady=5)

    # Bouton de vérification
    btn_check = ttk.Button(window, text="Vérifier", command=check_number)
    btn_check.pack(pady=10)

    # Résultat
    lbl_result = ttk.Label(window, text="", font=("Arial", 14, "bold"))
    lbl_result.pack(pady=10)

    # Affichage du score
    lbl_score = ttk.Label(window, text=f"Score : {score}", font=("Arial", 12, "bold"), foreground="blue")
    lbl_score.pack(pady=10)

    # Historique des vérifications
    ttk.Label(window, text="Historique :", font=("Arial", 12, "bold")).pack(pady=10)
    frame_history = ttk.Frame(window)
    frame_history.pack(pady=10, fill="both", expand=True)

    # Ajout d'une barre de défilement pour l'historique
    history_scrollbar = ttk.Scrollbar(frame_history, orient="vertical")
    history_list = tk.Listbox(frame_history, font=("Arial", 12), height=10, yscrollcommand=history_scrollbar.set)
    history_scrollbar.config(command=history_list.yview)

    history_list.pack(side="left", fill="both", expand=True)
    history_scrollbar.pack(side="right", fill="y")

    # Boutons supplémentaires
    btn_reset = ttk.Button(window, text="Réinitialiser", command=reset)
    btn_reset.pack(pady=10)

    btn_close = ttk.Button(window, text="Fermer", command=window.destroy)
    btn_close.pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    launch_tpx_6()
