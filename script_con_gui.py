import os
import os.path
import tkinter as tk

def controlla_oggetto_in_categorie(oggetto):
    categorie = ["R1", "R2", "R3", "R4", "R5"]
    presente = False

    for categoria in categorie:
        file_categoria = categoria + ".txt"
        if os.path.isfile(file_categoria):
            with open(file_categoria, 'r') as file:
                righe = file.readlines()
                righe_pulite = [riga.strip() for riga in righe]
                if oggetto.upper() in righe_pulite and oggetto != "":
                    risultato_label.config(text=f"L'oggetto '{oggetto}' deve essere buttato nella categoria '{categoria}'.", foreground="green")
                    presente = True

    if not presente:
        risultato_label.config(text=f"L'oggetto '{oggetto}' non è presente in nessuna categoria.", foreground="red")


def lancia_controlla_oggetto():
    oggetto = oggetto_entry.get()
    controlla_oggetto_in_categorie(oggetto)

root = tk.Tk()
root.title("Controllo Rifiuti")

oggetto_label = tk.Label(root, text="Inserisci il nome dell'oggetto da rifiutare:")
oggetto_label.pack()

oggetto_entry = tk.Entry(root)
oggetto_entry.pack()

controlla_button = tk.Button(root, text="Controlla", command=lancia_controlla_oggetto)
controlla_button.pack()

risultato_label = tk.Label(root)
risultato_label.pack()

root.mainloop()