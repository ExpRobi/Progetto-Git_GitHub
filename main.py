import os
import os.path

def controlla_categoria(oggetto):
    categorie = ["R1", "R2", "R3", "R4", "R5"]
    presente = False
    for categoria in categorie:
        file_categoria = categoria + ".txt"
        if os.path.isfile(file_categoria):
            with open(file_categoria, 'r') as file:
                contenuto = file.read()
                if oggetto.upper() in contenuto:
                    print(f"L'oggetto '{oggetto}' deve essere buttato nella categoria '{categoria}'.")
                    presente = True
                    x = open('lista.txt', 'a')
                    x.writelines(f"{oggetto.upper()}, {categoria} \n")
                    
    if not presente:
        print(f"L'oggetto '{oggetto}' non è presente in nessuna categoria.")

def main():
    oggetto = input("Inserisci il nome dell'oggetto da rifiutare: ")
    controlla_categoria(oggetto)

main()