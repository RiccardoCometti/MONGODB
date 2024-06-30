#(FORNARA, MI SCUSO PER NON AVERE COLLABORATO MA HO MOLTI IMPEGNI FAMILIARI)


import main
import json
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId

conn_uri = "mongodb+srv://RiccardoCometti:LoZioPera@clusterriccardocometti.sfhv7sz.mongodb.net/"

db_client = MongoClient(conn_uri, server_api=ServerApi('1'))

try:
    db_client.admin.command("effettuare il collegamento")
    print("collegato")
except Exception as err:
    print(err)
db_client.get_database('Esame_MONGO_DB').get_collection('Concerti').find_one

database = db_client["Esame_MONGO_DB"]
concerti_collezione = database["concerti"]
biglietti_collezione = database["biglietti"]  

def cerca_evento():
    print("""Per cercare il concerto in base a:
    1. album
    2. artista
    3. ospite""")
    opzione = input()

    if opzione == "1":
        criterio = "album"
        parametro_ricerca = input("album: ")
    elif opzione == "2":
        criterio = "artista"
        parametro_ricerca = input("artista: ")
    elif opzione == "3":
        criterio = "ospiti"
        parametro_ricerca = input("ospite: ")
    else:
        print("inserire un numero tra (1, 2, 3) per proseguire")
        return

    ricerca = {criterio: parametro_ricerca}
    risultati = concerti_collezione.find(ricerca)
    conteggio = concerti_collezione.count_documents(ricerca)

    risultati_lista = list(risultati)
    if len(risultati_lista) > 0:
        print("disponibilità:")
        for idx, risultato in enumerate(risultati_lista):
            print(f"{idx + 1}: Data: {risultato['data']}, Ora: {risultato['ora']}, città/stadio/piazza: {risultato['luogo concerto']}, nome artista: {risultato['artista']}, album: {risultato['nome album']}, ospiti: {risultato['ospiti']}, disponibilità: {risultato['disponibilità']}, prezzo: {risultato['prezzo']}€")
        
        
        selezione_idx = int(input("Seleziona il numero del concerto e acquista i biglietti: ")) - 1
        if selezione_idx < 0 or selezione_idx >= len(risultati_lista):
            print("opzione non valida.")
            return

        evento_selezionato = risultati_lista[selezione_idx]
        print(f"Concerto: {evento_selezionato['album']}, {evento_selezionato['data']}, {evento_selezionato['ora']}, {evento_selezionato['posizione concerto']}")

        
        acquista_biglietti(evento_selezionato)
    else:
        print("concerto non trovato.")

def acquista_biglietti(evento):
    if evento["disponibilità"] == 0:
        print("sold-out.")
        return

    conferma_acquisto = input("Confermare? (y/n): ").lower()
    if conferma_acquisto != "y":
        print("nullo.")
        return

    lista_biglietti = []
    for i in range(quantita_biglietti):
        numero_seriale = str(ObjectId())
        biglietto = {"id-evento": evento["_id"],
            "evento": evento["nome album"],
            "numero-serie": numero_seriale,
            "città/stadio/piazza": evento["luogo del concerto"],
            "data": evento["data"],
            "ora": evento["ora"],
        }
        lista_biglietti.append(biglietto)
        print(f"biglietto: {numero_seriale}")
    quantita_biglietti = int(input("numero biglietti"))
    if quantita_biglietti > evento["disponibilità"]:
        print("non disponibile.")
        return

    totale_pagare = quantita_biglietti * evento["prezzo"]
    print(f"conto: {totale_pagare}€")

    nuova_disponibilita = evento["disponibilità"] - quantita_biglietti
    concerti_collezione.update_one(
        {"_id": evento["_id"]},
        {"$set": {"disponibilità": nuova_disponibilita}}
    )
    biglietti_collezione.insert_many(lista_biglietti)
    print(f"nuove disponibilità: {nuova_disponibilita}")
cerca_evento()
