import os
import os.path
import tkinter as tk
from tkinter import messagebox, simpledialog
import getpass
import webbrowser
from functools import partial
from datetime import datetime
oggetto_entry = None


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
                    x.writelines(f"oggetto = {oggetto.upper()}, categoria = {categoria}, data di inserimento dell'oggetto = {datetime.today()}\n")
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

def chiudi_programma(event):
    root.quit()

def salva_nome_utente(nome_utente):
    with open("user.rsse", "w") as file:
        file.write(nome_utente)

def leggi_nome_utente():
    nome_utente = ""
    file = open("user.rsse", 'r')
    nome_utente = file.readline()
    return nome_utente

def set_focus(widget):
    widget.focus_set()

def mostra_dialogo_benvenuto():
    nome_utente = leggi_nome_utente()

    if nome_utente == "":
        messagebox.showinfo("Benvenuto", f"Ciao ({getpass.getuser()}), è la prima volta che utilizzi il programma?")
        risposta = messagebox.askyesno("Conferma", "È il tuo nome?")
        if risposta:
            nome_utente = getpass.getuser()
            salva_nome_utente(nome_utente)
        else:
            nome_utente = simpledialog.askstring("Inserisci il tuo nome", "Inserisci il tuo nome:")
            salva_nome_utente(nome_utente)
    else:
        messagebox.showinfo("Benvenuto", f"Ciao {nome_utente},")
        risposta = messagebox.askyesno("Conferma", "È la prima volta che usi il programma?")
        if risposta:
            webbrowser.open("https://github.com/ExpRobi/Progetto-Git_GitHub/tree/main#usage")
        else:
            print()

    root.after(0, lambda: set_focus(oggetto_entry))

    return nome_utente


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

nome_utente = mostra_dialogo_benvenuto()

oggetto_label = tk.Label(root, text="Inserisci il nome dell'oggetto da rifiutare:")
oggetto_label.pack()

oggetto_entry = tk.Entry(root)
oggetto_entry.pack()
oggetto_entry.bind('<Return>', controlla_oggetto)

oggetto_entry.focus()  # Imposta il focus sull'entry widget

controlla_button = tk.Button(root, text="Controlla", command=controlla_oggetto)
controlla_button.pack()

risultato_label = tk.Label(root)
risultato_label.pack()

root.bind('<Control-w>', chiudi_programma)  # Rileva la combinazione di tasti Ctrl+W per chiudere il programma

root.mainloop()
