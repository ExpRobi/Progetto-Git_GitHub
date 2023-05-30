import os
import os.path
import tkinter as tk
from tkinter import messagebox

def controlla_categorie(oggetto):
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
                    x = open('lista.txt', 'a')
                    x.writelines(f"{oggetto.upper()}, {categoria}\n")
                    controlla_button.config(state="disabled")  # Disabilita il pulsante "Controlla"
                    oggetto_entry.config(state="disabled")  # Disabilita l'entry widget
                    root.after(5000, abilita_controlla)
                    break  # Esci dal ciclo se l'oggetto è stato trovato
    if not presente:
        risultato_label.config(text=f"L'oggetto '{oggetto}' non è presente in nessuna categoria.", foreground="red")

def abilita_controlla():
    controlla_button.config(state="normal")  # Riabilita il pulsante "Controlla"
    oggetto_entry.config(state="normal")  # Riabilita l'entry widget

def controlla_oggetto(event=None):
    oggetto = oggetto_entry.get()
    controlla_categorie(oggetto)

root = tk.Tk()
root.title("Controllo Rifiuti")
# Inserisci il percorso completo dell'immagine del tuo logo o assicurati che sia nella stessa directory del file Python
logo_path = "logo.png"
# Carica l'immagine del logo
logo_image = tk.PhotoImage(file=logo_path)
logo_image = logo_image.subsample(2)  # Ridimensiona l'immagine del logo (fattore di sottocampionamento 2)
# Crea una label per visualizzare il logo
logo_label = tk.Label(root, image=logo_image)
logo_label.pack()
oggetto_label = tk.Label(root, text="Inserisci il nome dell'oggetto da rifiutare:")
oggetto_label.pack()
oggetto_entry = tk.Entry(root)
oggetto_entry.pack()
oggetto_entry.bind('<Return>', controlla_oggetto)
controlla_button = tk.Button(root, text="Controlla", command=controlla_oggetto)
controlla_button.pack()
risultato_label = tk.Label(root)
risultato_label.pack()
root.mainloop()