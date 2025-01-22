import tkinter as tk
from tkinter import ttk, messagebox

def launch_tpx_1():
    def convert():
        try:
            temp = float(entry_temp.get())
            input_scale = from_scale.get()
            output_scale = to_scale.get()

            if input_scale == output_scale:
                result = temp  
            else:
                # Convertir d'abord en Celsius
                if input_scale == "Fahrenheit":
                    temp_celsius = (temp - 32) * 5 / 9
                elif input_scale == "Kelvin":
                    temp_celsius = temp - 273.15
                elif input_scale == "Réaumur":
                    temp_celsius = temp * 5 / 4
                else:
                    temp_celsius = temp  

                # Convertir de Celsius vers l'échelle de sortie
                if output_scale == "Fahrenheit":
                    result = (temp_celsius * 9 / 5) + 32
                elif output_scale == "Kelvin":
                    result = temp_celsius + 273.15
                elif output_scale == "Réaumur":
                    result = temp_celsius * 4 / 5
                else:
                    result = temp_celsius  
                    
            lbl_result.config(text=f"{temp} {input_scale} = {result:.2f} {output_scale}")
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer une température valide.")

    window = tk.Tk()
    window.title("Conversion de Température")
    window.geometry("600x400")
    window.resizable(False, False)

    ttk.Label(window, text="TP1 : Conversion entre plusieurs échelles de température", font=("Arial", 14, "bold")).pack(pady=10)
    ttk.Label(window, text="Entrez une température et choisissez les échelles de conversion :", font=("Arial", 12)).pack(pady=10)

    entry_temp = ttk.Entry(window, font=("Arial", 12), width=20, justify="center")
    entry_temp.pack(pady=5)

    # Choix des échelles de température
    scales = ["Celsius", "Fahrenheit", "Kelvin", "Réaumur"]

    ttk.Label(window, text="De :", font=("Arial", 12)).pack(pady=5)
    from_scale = ttk.Combobox(window, values=scales, font=("Arial", 12), state="readonly", width=15)
    from_scale.current(0)
    from_scale.pack(pady=5)

    ttk.Label(window, text="Vers :", font=("Arial", 12)).pack(pady=5)
    to_scale = ttk.Combobox(window, values=scales, font=("Arial", 12), state="readonly", width=15)
    to_scale.current(1)
    to_scale.pack(pady=5)

    # Bouton de conversion
    btn_convert = ttk.Button(window, text="Convertir", command=convert)
    btn_convert.pack(pady=10)

    # Résultat de la conversion
    lbl_result = ttk.Label(window, text="", font=("Arial", 14, "bold"), foreground="blue")
    lbl_result.pack(pady=20)

    # Bouton de fermeture
    ttk.Button(window, text="Fermer", command=window.destroy).pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    launch_tpx_1()
