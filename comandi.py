#file per richiamare le funzioni e interfaccia
import main

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://RiccardoCometti:LoZioPera@clusterriccardocometti.sfhv7sz.mongodb.net/"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)



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