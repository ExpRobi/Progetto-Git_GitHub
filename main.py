import os
import datetime


""" fare un programma in python che smista i rifiuti è i rifiuti smaltiti vengono salvati in un file in modalità (append) con timestamp della data corrente alla richiesta

    R1-Grande bianco freddo -grandi elettrodomestici per la refrigerazione: frigoriferi, congelatori, condizionatori
    R2-Grande bianco non freddo -grandi elettrodomestici come lavatrici, lavastoviglie.
    R3-TV Monitor a tubo catodico
    R4-Elettronica di consumo, Telecomunicazioni, Informatica, piccoli elettrodomestici, elettroutensili, giocattoli, apparecchi di illuminazione, dispositivi medici.
    R5-Sorgenti luminose a scarica: lampade fluorescenti e sorgenti luminose compatte.


    il programma deve mandare ogni fine aggiunta del rifiuto il file Rifiuti[QUI LA CATEGORIA DEL RIFIUTO] e deve metterlo nella reposotory "Progetto-Git_GitHub"


"""
import os.path
import datetime

# lista delle possibili categorie
categorie = ["R1", "R2", "R3", "R4", "R5"]

# richiesta di selezionare una delle categorie
categoria = ""
while categoria not in categorie:
    categoria = input(f"Seleziona una delle seguenti categorie: {categorie}\n")
    categoria = categoria.upper()
    match categoria:
        case 'R1':
            while True:
                print("Grande bianco freddo -grandi elettrodomestici per la refrigerazione: frigoriferi, congelatori, condizionatori")
                oggetto = str(input("Inserisci il nome dell'oggetto da rifiutare: "))
                if "/" in oggetto or "\\" in oggetto:
                    print("Il nome dell'oggetto non può contenere i caratteri '/' o '\'.")
                else:
                    file_categoria = categoria + ".txt"
                with open(file_categoria, 'a') as file:
                 # TimeStamp
                    timestamp = datetime.datetime.now().isoformat()
                    file.write(f"DATA:{timestamp} OGGETTO: {oggetto.upper()}\n")

                    print(f"Il nome dell'oggetto '{oggetto}' è stato aggiunto al file '{file_categoria}'.")
                    break
        case 'R2':
            while True:
                print("Grande bianco non freddo -grandi elettrodomestici come lavatrici, lavastoviglie.")
                oggetto = str(input("Inserisci il nome dell'oggetto da rifiutare: "))
                if "/" in oggetto or "\\" in oggetto:
                    print("Il nome dell'oggetto non può contenere i caratteri '/' o '\'.")
                else:
                    file_categoria = categoria + ".txt"
                with open(file_categoria, 'a') as file:
                 # TimeStamp
                    timestamp = datetime.datetime.now().isoformat()
                    file.write(f"DATA:{timestamp} OGGETTO: {oggetto.upper()}\n")

                    print(f"Il nome dell'oggetto '{oggetto}' è stato aggiunto al file '{file_categoria}'.")
                    break
        case 'R3':
            while True:
                print("TV o Monitor a tubo catodico")
                oggetto = str(input("Inserisci il nome dell'oggetto da rifiutare: "))
                oggetto = oggetto.lower()
                if oggetto == "tv a tubo catodico" or oggetto == "monitor a tubo catodico":
                    if "/" in oggetto or "\\" in oggetto:
                        print("Il nome dell'oggetto non può contenere i caratteri '/' o '\'.")
                    else:
                        file_categoria = categoria + ".txt"
                    with open(file_categoria, 'a') as file:
                    # TimeStamp
                        timestamp = datetime.datetime.now().isoformat()
                        file.write(f"DATA:{timestamp} OGGETTO: {oggetto.upper()}\n")

                        print(f"Il nome dell'oggetto '{oggetto}' è stato aggiunto al file '{file_categoria}'.")
                        break
                else:
                    print()
        case 'R4':
            while True:
                print("Elettronica di consumo, Telecomunicazioni, Informatica, piccoli elettrodomestici, elettroutensili, giocattoli, apparecchi di illuminazione, dispositivi medici.")
                oggetto = str(input("Inserisci il nome dell'oggetto da rifiutare: "))
                if "/" in oggetto or "\\" in oggetto:
                    print("Il nome dell'oggetto non può contenere i caratteri '/' o '\'.")
                else:
                    file_categoria = categoria + ".txt"
                with open(file_categoria, 'a') as file:
                 # TimeStamp
                    timestamp = datetime.datetime.now().isoformat()
                    file.write(f"DATA:{timestamp} OGGETTO: {oggetto.upper()}\n")

                    print(f"Il nome dell'oggetto '{oggetto}' è stato aggiunto al file '{file_categoria}'.")
                    break
        case 'R5':
            while True:
                print("Sorgenti luminose a scarica: lampade fluorescenti e sorgenti luminose compatte.")
                oggetto = str(input("Inserisci il nome dell'oggetto da rifiutare: "))
                if "/" in oggetto or "\\" in oggetto:
                    print("Il nome dell'oggetto non può contenere i caratteri '/' o '\'.")
                else:
                    file_categoria = categoria + ".txt"
                with open(file_categoria, 'a') as file:
                 # TimeStamp
                    timestamp = datetime.datetime.now().isoformat()
                    file.write(f"DATA:{timestamp} OGGETTO: {oggetto.upper()}\n")

                    print(f"Il nome dell'oggetto '{oggetto}' è stato aggiunto al file '{file_categoria}'.")
                    break
