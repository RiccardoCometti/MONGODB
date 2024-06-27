#COMANDI.PY è il file per richiamare le funzioni e interfaccia

###### IMPORT ######################################################################################
import main

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

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
