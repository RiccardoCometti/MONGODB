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
# Definizione del database e la collezione
db = client["Eseame_MONGO_DB"]
concerti_collection = db["Concerti"]
biglietti_collection = db["Biglietti"]  # Aggiunto per la collezione dei biglietti

def carica_dati():
    with open('DatasetConcerti.json') as file:
        dati = json.load(file)
        concerti_collection.insert_many(dati)

# Funzione per cercare i concerti direttamente dalla collezione "Concerti"
def cerca_concerto():
    
    client = MongoClient(uri, server_api=ServerApi("1"))
    db = client["Eseame_MONGO_DB"]  #per connettersi al database
    lista_concerti = db["Concerti"]  #per connettersi alla collection
    
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
    risultati = lista_concerti.find(query)
    count = lista_concerti.count_documents(query)
    
    risultati_lista = list(risultati)
    if len(risultati_lista) > 0:
        print("Risultati disponibili:")
        for risultato in risultati_lista:
            print(f"Data: {risultato['data']}, Ora: {risultato['ora']}, Luogo: {risultato['luogo del concerto']}, Artista: {risultato['artista']}, Album: {risultato['nome album']}, Ospiti: {risultato['ospiti']}")
    else:
        print("Nessun risultato trovato.")


cerca_concerto()

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
    concerti_collection.update_one(
        {"_id": concerto["_id"]},
        {"$set": {"disponibilità": nuova_disponibilità}}
    )
    biglietti_collection.insert_many(biglietti)  # Inserimento dei biglietti nella collezione
    print(f"Disponibilità aggiornata: {nuova_disponibilità}")
