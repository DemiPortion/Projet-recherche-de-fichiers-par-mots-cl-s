import tkinter as tk
from tp_2_1 import tp_2_1
from tp_2_2 import tp_2_2
from tp_2_3 import tp_2_3
from tp_2_4 import tp_2_4
from tp_2_5 import tp_2_5
from tp_2_6 import tp_2_6

def main():
    root = tk.Tk()
    root.title("Gestionnaire des TP")
    root.geometry("400x300")

    tk.Label(root, text="Choisissez un TP :", font=("Arial", 14)).pack(pady=20)

    tk.Button(root, text="TP 2.1 : Simulation de dés", command=tp_2_1).pack(pady=5)
    tk.Button(root, text="TP 2.2 : Moyenne et Médiane", command=tp_2_2).pack(pady=5)
    tk.Button(root, text="TP 2.3 : Variance et Écart-type", command=tp_2_3).pack(pady=5)
    tk.Button(root, text="TP 2.4 : Bateau", command=tp_2_4).pack(pady=5)
    tk.Button(root, text="TP 2.5 : Port", command=tp_2_5).pack(pady=5)
    tk.Button(root, text="TP 2.6 : Liste de Camping", command=tp_2_6).pack(pady=5)

    tk.Button(root, text="Quitter", command=root.quit).pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
