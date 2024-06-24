#file per richiamare le funzioni e interfaccia
import main
from pymongo import MongoClient

uriMongoDb = "mongodb+srv://RiccardoCometti:LoZioPera@clusterriccardocometti.sfhv7sz.mongodb.net/"


client = MongoClient(uriMongoDb)

DataBase =  client["Esame_MONGO_DB"]            #accesso al Dataset
collection = DataBase["Concerti"]               #accesso alla collection



print("""per cercare il concerto in base:
      all'artista: 1
      all'album: 2
      all'ospite: 3""")
scelta = input()


if scelta == "1":
    print(input("Inserisci il nome dell'artista: "))
elif scelta == "2":
    print(input("Inserisci il nome dell'album: "))
elif scelta == "3":
    print(input("Inserisci il nome dell'ospite: "))
else:
    print("errore")

    #da inserire le funzioni per la ricerca