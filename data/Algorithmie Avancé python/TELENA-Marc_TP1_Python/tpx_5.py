import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

def launch_tpx_5():
    def check_leap_year():
        year = entry_year.get()
        if not year.isdigit():
            messagebox.showwarning("Erreur", "Veuillez entrer une année valide.")
            return
        year = int(year)
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            messagebox.showinfo("Résultat", f"{year} est une année bissextile.")
        else:
            messagebox.showerror("Résultat", f"{year} n'est pas une année bissextile.")

    def calculate_leap_years():
        current_year = 2024  # Jusqu'en 2024
        leap_years = [year for year in range(1, current_year + 1) if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)]
        return leap_years

    def display_leap_years():
        leap_years = calculate_leap_years()
        # Supprime les anciennes données du tableau
        for row in table.get_children():
            table.delete(row)
        # Ajoute les années dans le tableau
        for i, year in enumerate(leap_years, start=1):
            table.insert("", "end", values=(i, year))

    def search_year():
        search_value = entry_search.get()
        if not search_value.isdigit():
            messagebox.showwarning("Erreur", "Veuillez entrer une année valide à rechercher.")
            return
        search_value = int(search_value)
        
        # Recherche dans le tableau
        for row in table.get_children():
            item = table.item(row, "values")
            if int(item[1]) == search_value:
                table.selection_set(row)
                table.see(row)
                messagebox.showinfo("Résultat", f"L'année {search_value} est trouvée dans la liste.")
                return
        messagebox.showerror("Résultat", f"L'année {search_value} n'est pas trouvée dans la liste.")

    window = tk.Tk()
    window.title("Année Bissextile")
    window.geometry("700x700")
    window.resizable(False, False)

    # Cadre principal avec scrollbar pour tout le contenu
    main_frame = ttk.Frame(window)
    main_frame.pack(fill="both", expand=True)

    canvas = tk.Canvas(main_frame)
    scrollbar_y = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
    scrollbar_y.pack(side="right", fill="y")
    frame_content = ttk.Frame(canvas)

    canvas.create_window((0, 0), window=frame_content, anchor="center")
    canvas.configure(yscrollcommand=scrollbar_y.set)

    def on_frame_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    frame_content.bind("<Configure>", on_frame_configure)

    canvas.pack(side="left", fill="both", expand=True)

    # Contenu centré
    ttk.Label(frame_content, text="TP5 : Vérification des années bissextiles", font=("Arial", 14, "bold")).pack(pady=10)
    ttk.Label(frame_content, text="Entrez une année pour vérifier si elle est bissextile :", font=("Arial", 12)).pack(pady=10)

    entry_year = ttk.Entry(frame_content, font=("Arial", 12), width=20, justify="center")
    entry_year.pack(pady=5)

    btn_check = ttk.Button(frame_content, text="Vérifier", command=check_leap_year)
    btn_check.pack(pady=10)

    ttk.Label(frame_content, text="Liste des années bissextiles jusqu'en 2024 :", font=("Arial", 12, "bold")).pack(pady=10)

    # Tableau des années bissextiles
    frame_table = ttk.Frame(frame_content)
    frame_table.pack(pady=10, fill="both", expand=True)

    scrollbar_table = ttk.Scrollbar(frame_table, orient="vertical")
    scrollbar_table.pack(side="right", fill="y")

    columns = ("#", "Année")
    table = ttk.Treeview(frame_table, columns=columns, show="headings", height=15, yscrollcommand=scrollbar_table.set)
    table.heading("#", text="N°")
    table.heading("Année", text="Année")
    table.column("#", width=50, anchor="center")
    table.column("Année", width=150, anchor="center")
    table.pack(side="left", fill="both", expand=True)

    scrollbar_table.config(command=table.yview)

    btn_display = ttk.Button(frame_content, text="Afficher les années bissextiles", command=display_leap_years)
    btn_display.pack(pady=10)

    ttk.Label(frame_content, text="Recherche d'une année :", font=("Arial", 12)).pack(pady=10)

    entry_search = ttk.Entry(frame_content, font=("Arial", 12), width=20, justify="center")
    entry_search.pack(pady=5)

    btn_search = ttk.Button(frame_content, text="Rechercher", command=search_year)
    btn_search.pack(pady=10)

    # Bouton Fermer toujours visible
    btn_close = ttk.Button(window, text="Fermer", command=window.destroy)
    btn_close.pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    launch_tpx_5()
