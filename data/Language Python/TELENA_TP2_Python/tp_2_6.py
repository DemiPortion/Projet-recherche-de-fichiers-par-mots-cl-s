import tkinter as tk
from tkinter import ttk, messagebox, filedialog

def tp_2_6():
    def add_item():
        item = entry_item.get()
        if item:
            camping_list.append(item)
            refresh_list()
            entry_item.delete(0, tk.END)
        else:
            messagebox.showerror("Erreur", "Veuillez entrer un article valide.")

    def remove_item():
        selected = listbox.curselection()
        if selected:
            camping_list.pop(selected[0])
            refresh_list()
        else:
            messagebox.showerror("Erreur", "Veuillez sélectionner un article à supprimer.")

    def mark_essential():
        selected = listbox.curselection()
        if selected:
            index = selected[0]
            camping_list[index] += " (Indispensable)"
            refresh_list()
        else:
            messagebox.showerror("Erreur", "Veuillez sélectionner un article à marquer comme indispensable.")

    def save_list():
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Fichiers texte", "*.txt")],
            title="Enregistrer la liste"
        )
        if file_path:
            try:
                with open(file_path, "w") as file:
                    file.write("\n".join(camping_list))
                messagebox.showinfo("Succès", "Liste sauvegardée avec succès!")
            except Exception as e:
                messagebox.showerror("Erreur", f"Impossible de sauvegarder la liste : {e}")

    def load_list():
        file_path = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("Fichiers texte", "*.txt")],
            title="Charger une liste"
        )
        if file_path:
            try:
                with open(file_path, "r") as file:
                    items = file.read().splitlines()
                    # Mettre à jour la liste globale
                    camping_list.clear()
                    camping_list.extend(items)
                    refresh_list()
                messagebox.showinfo("Succès", "Liste chargée avec succès!")
            except Exception as e:
                messagebox.showerror("Erreur", f"Impossible de charger la liste : {e}")

    def refresh_list():
        listbox.delete(0, tk.END)
        for item in camping_list:
            listbox.insert(tk.END, item)

    def close_window():
        window.destroy()

    # Liste d'articles
    camping_list = []

    # Fenêtre principale
    window = tk.Toplevel()
    window.title("TP 2.6 : Liste de Camping")
    window.geometry("800x600")
    window.configure(bg="#f2f2f2")

    frame = ttk.Frame(window, padding=20)
    frame.pack(expand=True)

    # Entrée pour ajouter des articles
    ttk.Label(frame, text="Article à ajouter :", font=("Arial", 14)).pack(pady=10)
    entry_item = ttk.Entry(frame, width=40)
    entry_item.pack(pady=10)

    # Boutons pour gérer la liste
    ttk.Button(frame, text="Ajouter Article", command=add_item).pack(pady=10)
    ttk.Button(frame, text="Supprimer Article", command=remove_item).pack(pady=10)
    ttk.Button(frame, text="Marquer comme Indispensable", command=mark_essential).pack(pady=10)

    # Liste des articles
    ttk.Label(frame, text="Liste des articles :", font=("Arial", 14)).pack(pady=10)
    listbox = tk.Listbox(frame, width=60, height=10)
    listbox.pack(pady=10)

    # Boutons pour sauvegarder et charger la liste
    ttk.Button(frame, text="Sauvegarder la Liste", command=save_list).pack(pady=10)
    ttk.Button(frame, text="Charger la Liste", command=load_list).pack(pady=10)

    # Bouton pour quitter
    ttk.Button(frame, text="Quitter", command=close_window).pack(pady=20)
