#COMANDI.PY è il file per richiamare le funzioni e interfaccia

###### IMPORT ######################################################################################
import main
import json

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId


######### CONNESSIONE A MONGODB #####################################################################
uri = "mongodb+srv://RiccardoCometti:LoZioPera@clusterriccardocometti.sfhv7sz.mongodb.net/"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
#######################################################################################################
#client.get_database('Esame_MONGO_DB').get_collection('Concerti').find_one

# definizione del database e la collezione
db = client["Esame_MONGO_DB"]
concerti_collection = db["Concerti"]
biglietti_collection = db["Biglietti"]  # Aggiunto per la collezione dei biglietti


# Funzione per cercare i concerti direttamente dalla collezione "Concerti"
def cerca_concerto():
    print("""Per cercare il concerto in base a:
    1. Artista
    2. Album
    3. Ospite""")
    scelta = input()

    if scelta == "1":
        finalita = "artista"
        metodo_ricerca = input("Inserisci il nome dell'artista: ")
    elif scelta == "2":
        finalita = "nome album"
        metodo_ricerca = input("Inserisci il nome dell'album: ")
    elif scelta == "3":
        finalita = "ospiti"
        metodo_ricerca = input("Inserisci il nome dell'ospite: ")
    else:
        print("Errore, seleziona un numero tra 1, 2 o 3")
        return

    query = {finalita: metodo_ricerca}
    risultati = concerti_collection.find(query)  # Modifica: Cerca direttamente nella collezione "Concerti"
    count = concerti_collection.count_documents(query)  # Modifica: Conta i documenti nella collezione "Concerti"

    risultati_lista = list(risultati)
    if len(risultati_lista) > 0:
        print("Risultati disponibili:")
        for idx, risultato in enumerate(risultati_lista):
            print(f"{idx + 1}: Data: {risultato['data']}, Ora: {risultato['ora']}, Luogo: {risultato['luogo del concerto']}, Artista: {risultato['artista']}, Album: {risultato['nome album']}, Ospiti: {risultato['ospiti']}, Disponibilità: {risultato['disponibilità']}, Prezzo: {risultato['prezzo']}€")
        
        # Selezione del concerto
        index = int(input("Seleziona il numero del concerto per visualizzare i dettagli e acquistare i biglietti: ")) - 1
        if index < 0 or index >= len(risultati_lista):
            print("Selezione non valida.")
            return

        concerto_selezionato = risultati_lista[index]
        print(f"Concerto selezionato: {concerto_selezionato['nome album']}, {concerto_selezionato['data']}, {concerto_selezionato['ora']}, {concerto_selezionato['luogo del concerto']}")

        # Acquisto biglietti
        acquista_biglietti(concerto_selezionato)  # Modifica: Passa il concerto selezionato alla funzione di acquisto
    else:
        print("Nessun risultato trovato.")

def acquista_biglietti(concerto):
    if concerto["disponibilità"] == 0:
        print("Il concerto è sold-out.")
        return

    quantita = int(input("Quanti biglietti vuoi acquistare? "))
    if quantita > concerto["disponibilità"]:
        print("Quantità non disponibile.")
        return

    totale = quantita * concerto["prezzo"]
    print(f"Totale da pagare: {totale}€")

    conferma = input("Confermi l'acquisto? (s/n): ").lower()
    if conferma != "s":
        print("Acquisto annullato.")
        return

    # Generazione dei biglietti con numero di serie univoco
    biglietti = []
    for i in range(quantita):
        numero_serie = str(ObjectId())
        biglietto = {
            "numero_serie": numero_serie,
            "concerto_id": concerto["_id"],
            "nome_concerto": concerto["nome album"],
            "data": concerto["data"],
            "ora": concerto["ora"],
            "luogo": concerto["luogo del concerto"]
        }
        biglietti.append(biglietto)
        print(f"Biglietto emesso: {numero_serie}")

    # Aggiornamento disponibilità
    nuova_disponibilità = concerto["disponibilità"] - quantita
    concerti_collection.update_one(  # Modifica: Aggiorna direttamente la collezione "Concerti"
        {"_id": concerto["_id"]},
        {"$set": {"disponibilità": nuova_disponibilità}}
    )
    biglietti_collection.insert_many(biglietti)  # Modifica: Inserisce i biglietti nella collezione "Biglietti"
    print(f"Disponibilità aggiornata: {nuova_disponibilità}")

cerca_concerto()