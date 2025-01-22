import tkinter as tk
from tkinter import ttk, messagebox

def launch_tpx_2():
    def calculate():
        try:
            n = int(entry_number.get())
            if n <= 0:
                raise ValueError("Le nombre doit être positif.")
            
            even_numbers = [i for i in range(2, n + 1, 2)]
            sum_even = sum(even_numbers)
            product_even = 1
            for num in even_numbers:
                product_even *= num

            # Affichage formaté avec des titres
            result_text = (
                "===== SOMME =====\n"
                f"1. {' + '.join(map(str, even_numbers))} = {sum_even}\n"
                f"2. {sum_even} = {' + '.join(map(str, even_numbers))}\n\n"
                "===== PRODUIT =====\n"
                f"3. {' * '.join(map(str, even_numbers))} = {product_even}\n"
                f"4. {product_even} = {' * '.join(map(str, even_numbers))}"
            )

            lbl_result.config(text=result_text)
        except ValueError:
            messagebox.showwarning("Erreur", "Veuillez entrer un entier positif valide.")

    def reset():
        entry_number.delete(0, tk.END)
        lbl_result.config(text="")

    def ask_restart():
        if messagebox.askyesno("Recommencer", "Voulez-vous recommencer ?"):
            reset()
        else:
            window.destroy()

    window = tk.Tk()
    window.title("Somme et Produit des Nombres Pairs")
    window.geometry("600x550")
    window.resizable(False, False)

    # Titre principal
    ttk.Label(window, text="TP2 : Somme et Produit des Nombres Pairs", font=("Arial", 16, "bold")).pack(pady=10)

    # Entrée de l'entier positif
    ttk.Label(window, text="Entrez un entier positif :", font=("Arial", 12)).pack(pady=10)
    entry_number = ttk.Entry(window, font=("Arial", 12), width=20, justify="center")
    entry_number.pack(pady=5)

    # Bouton de calcul
    btn_calculate = ttk.Button(window, text="Calculer", command=calculate)
    btn_calculate.pack(pady=10)

    # Zone d'affichage des résultats
    lbl_result = ttk.Label(window, text="", font=("Arial", 12), justify="left", anchor="center")
    lbl_result.pack(pady=20)

    # Boutons d'options
    btn_reset = ttk.Button(window, text="Recommencer", command=ask_restart)
    btn_reset.pack(pady=10)

    btn_close = ttk.Button(window, text="Fermer", command=window.destroy)
    btn_close.pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    launch_tpx_2()
