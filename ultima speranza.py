import pymongo 
from pymongo import MongoClient
from bson.objectid import ObjectId
###########################################################
# terminale ####################################
import pyfiglet as p
from colorama import init, Fore, Back, Style 
from termcolor import colored
init(autoreset=True)
#################################################

client = MongoClient("mongodb://localhost:27017")
db = client.pymongo
concertiCollection = db.concerti

# concerti = [
#     {"_id": "1", "data": "2025-03-17", "ora": "15:57", "luogo del concerto": "Stadio Olimpico, Rome", "coordinate geografiche del concerto": "41.9339, 12.4540", "artista": "Zucchero", "nome album": "Black Cat", "costo del biglietto standard": 33, "costo del biglietto premium": 149, "ospiti": "Sting"},
#     {"_id": "2", "data": "2025-05-22", "ora": "20:00", "luogo del concerto": "Wembley Stadium, London", "coordinate geografiche del concerto": "51.5560, -0.2796", "artista": "Coldplay", "nome album": "A Head Full of Dreams", "costo del biglietto standard": 55, "costo del biglietto premium": 180 , "ospiti": "Rihanna"},
#     {"_id": "3", "data": "2025-07-10", "ora": "21:00", "luogo del concerto": "Madison Square Garden, New York", "coordinate geografiche del concerto": "40.7505, -73.9934", "artista": "Beyoncé", "nome album": "Lemonade", "costo del biglietto standard": 70, "costo del biglietto premium": 250, "ospiti": "Jay-Z"},
#     {"_id": "4", "data": "2025-09-15", "ora": "19:30", "luogo del concerto": "Allianz Arena, Munich", "coordinate geografiche del concerto": "48.2188, 11.6247", "artista": "Rammstein", "nome album": "Zeit", "costo del biglietto standard": 65, "costo del biglietto premium": 210, "ospiti": "Marilyn Manson"},
#     {"_id": "5", "data": "2025-11-25", "ora": "18:00", "luogo del concerto": "Parco Dora, Turin", "coordinate geografiche del concerto": "45.0957, 7.6667", "artista": "Elisa", "nome album": "Diari Aperti", "costo del biglietto standard": 40, "costo del biglietto premium": 120, "ospiti": "Ligabue"},
#     {"_id": "6", "data": "2025-08-30", "ora": "17:00", "luogo del concerto": "San Siro, Milan", "coordinate geografiche del concerto": "45.4781, 9.1240", "artista": "Vasco Rossi", "nome album": "Siamo Qui", "costo del biglietto standard": 50, "costo del biglietto premium": 200, "ospiti": "Modena City Ramblers"},
#     {"_id": "7", "data": "2025-04-12", "ora": "16:00", "luogo del concerto": "Olympiastadion, Berlin", "coordinate geografiche del concerto": "52.5145, 13.2395", "artista": "Ed Sheeran", "nome album": "Divide", "costo del biglietto standard": 60, "costo del biglietto premium": 190, "ospiti": "Anne-Marie"},
#     {"_id": "8", "data": "2025-06-05", "ora": "19:00", "luogo del concerto": "Camp Nou, Barcelona", "coordinate geografiche del concerto": "41.3809, 2.1228", "artista": "Shakira", "nome album": "El Dorado", "costo del biglietto standard": 45, "costo del biglietto premium": 170, "ospiti": "Maluma"},
#     {"_id": "9", "data": "2025-07-20", "ora": "20:30", "luogo del concerto": "Stade de France, Paris", "coordinate geografiche del concerto": "48.9244, 2.3601", "artista": "David Guetta", "nome album": "7", "costo del biglietto standard": 50, "costo del biglietto premium": 200, "ospiti": "Sia"},
#     {"_id": "10", "data": "2025-12-31", "ora": "23:00", "luogo del concerto": "Sydney Opera House, Sydney", "coordinate geografiche del concerto": "-33.8568, 151.2153", "artista": "Tame Impala", "nome album": "Currents", "costo del biglietto standard": 80, "costo del biglietto premium": 300, "ospiti": "Flume"},
#     {"_id": "11", "data": "2025-01-25", "ora": "20:00", "luogo del concerto": "O2 Arena, London", "coordinate geografiche del concerto": "51.5030, 0.0032", "artista": "Adele", "nome album": "30", "costo del biglietto standard": 85, "costo del biglietto premium": 220, "ospiti": "Sam Smith"},
#     {"_id": "12", "data": "2025-02-14", "ora": "19:30", "luogo del concerto": "Forum Assago, Milan", "coordinate geografiche del concerto": "45.4213, 9.1582", "artista": "Måneskin", "nome album": "Teatro d'ira - Vol. I", "costo del biglietto standard": 45, "costo del biglietto premium": 150, "ospiti": "Francesco Gabbani"},
#     {"_id": "13", "data": "2025-04-10", "ora": "21:00", "luogo del concerto": "Red Rocks Amphitheatre, Denver", "coordinate geografiche del concerto": "39.6654, -105.2057", "artista": "The Lumineers", "nome album": "III", "costo del biglietto standard": 60, "costo del biglietto premium": 200, "ospiti": "Mumford & Sons"},
#     {"_id": "14", "data": "2025-06-18", "ora": "20:00", "luogo del concerto": "Estadio Monumental, Buenos Aires", "coordinate geografiche del concerto": "-34.5456, -58.4492", "artista": "Luis Miguel", "nome album": "¡México Por Siempre!", "costo del biglietto standard": 40, "costo del biglietto premium": 150, "ospiti": "Alejandro Sanz"},
#     {"_id": "15", "data": "2025-08-12", "ora": "21:30", "luogo del concerto": "Plaza de Toros, Madrid", "coordinate geografiche del concerto": "40.4330, -3.7196", "artista": "Enrique Iglesias", "nome album": "Sex and Love", "costo del biglietto standard": 55, "costo del biglietto premium": 180, "ospiti": "Pitbull"},
#     {"_id": "16", "data": "2025-11-04", "ora": "19:00", "luogo del concerto": "The O2, London", "coordinate geografiche del concerto": "51.5030, 0.0032", "artista": "Dua Lipa", "nome album": "Future Nostalgia", "costo del biglietto standard": 70, "costo del biglietto premium": 210, "ospiti": "Calvin Harris"},
#     {"_id": "17", "data": "2025-05-07", "ora": "18:00", "luogo del concerto": "Stadio San Paolo, Naples", "coordinate geografiche del concerto": "40.8253, 14.1936", "artista": "Tiziano Ferro", "nome album": "Accetto Miracoli", "costo del biglietto standard": 50, "costo del biglietto premium": 160, "ospiti": "Laura Pausini"},
#     {"_id": "18", "data": "2025-09-21", "ora": "20:30", "luogo del concerto": "Arena di Verona, Verona", "coordinate geografiche del concerto": "45.4384, 10.9920", "artista": "Andrea Bocelli", "nome album": "Believe", "costo del biglietto standard": 80, "costo del biglietto premium": 250, "ospiti": "Céline Dion"},
#     {"_id": "19", "data": "2025-12-08", "ora": "19:30", "luogo del concerto": "Royal Albert Hall, London", "coordinate geografiche del concerto": "51.5009, -0.1774", "artista": "Elton John", "nome album": "Diamonds", "costo del biglietto standard": 90, "costo del biglietto premium": 300, "ospiti": "Billy Joel"},
#     {"_id": "20", "data": "2025-03-30", "ora": "18:00", "luogo del concerto": "Mediolanum Forum, Milan", "coordinate geografiche del concerto": "45.4213, 9.1582", "artista": "Jovanotti", "nome album": "Oh, vita!", "costo del biglietto standard": 50, "costo del biglietto premium": 150, "ospiti": "Fabri Fibra"},
#     {"_id": "21", "data": "2025-07-22", "ora": "20:00", "luogo del concerto": "Hyde Park, London", "coordinate geografiche del concerto": "51.5074, -0.1657", "artista": "Taylor Swift", "nome album": "Evermore", "costo del biglietto standard": 65, "costo del biglietto premium": 220, "ospiti": "HAIM"},
#     {"_id": "22", "data": "2025-08-15", "ora": "21:00", "luogo del concerto": "Dodger Stadium, Los Angeles", "coordinate geografiche del concerto": "34.0739, -118.2399", "artista": "Billie Eilish", "nome album": "Happier Than Ever", "costo del biglietto standard": 75, "costo del biglietto premium": 250, "ospiti": "Finneas"},
#     {"_id": "23", "data": "2025-05-25", "ora": "19:00", "luogo del concerto": "Olympic Stadium, Athens", "coordinate geografiche del concerto": "38.0527, 23.7910", "artista": "Muse", "nome album": "Simulation Theory", "costo del biglietto standard": 55, "costo del biglietto premium": 180, "ospiti": "30 Seconds to Mars"},
#     {"_id": "24", "data": "2025-10-31", "ora": "20:30", "luogo del concerto": "Gocheok Sky Dome, Seoul", "coordinate geografiche del concerto": "37.4982, 126.8679", "artista": "BTS", "nome album": "Map of the Soul: 7", "costo del biglietto standard": 90, "costo del biglietto premium": 300, "ospiti": "Halsey"},
#     {"_id": "25", "data": "2025-11-11", "ora": "20:00", "luogo del concerto": "Madison Square Garden, New York", "coordinate geografiche del concerto": "40.7505, -73.9934", "artista": "Bruno Mars", "nome album": "24K Magic", "costo del biglietto standard": 80, "costo del biglietto premium": 300, "ospiti": "Anderson .Paak"},
#     {"_id": "26", "data": "2025-07-18", "ora": "19:00", "luogo del concerto": "Stadio Artemio Franchi, Florence", "coordinate geografiche del concerto": "43.7807, 11.2821", "artista": "Laura Pausini", "nome album": "Fatti Sentire", "costo del biglietto standard": 45, "costo del biglietto premium": 160, "ospiti": "Biagio Antonacci"},
#     {"_id": "27", "data": "2025-12-22", "ora": "18:30", "luogo del concerto": "Rod Laver Arena, Melbourne", "coordinate geografiche del concerto": "-37.8216, 144.9786", "artista": "Sia", "nome album": "This Is Acting", "costo del biglietto standard": 60, "costo del biglietto premium": 200, "ospiti": "Diplo"},
#     {"_id": "28", "data": "2025-09-30", "ora": "19:30", "luogo del concerto": "AccorHotels Arena, Paris", "coordinate geografiche del concerto": "48.8383, 2.3780", "artista": "Camila Cabello", "nome album": "Romance", "costo del biglietto standard": 50, "costo del biglietto premium": 180, "ospiti": "Shawn Mendes"},
#     {"_id": "29", "data": "2025-04-05", "ora": "17:00", "luogo del concerto": "Ziggo Dome, Amsterdam", "coordinate geografiche del concerto": "52.3143, 4.9374", "artista": "Imagine Dragons", "nome album": "Evolve", "costo del biglietto standard": 55, "costo del biglietto premium": 200, "ospiti": "Kings of Leon"},
#     {"_id": "30", "data": "2025-06-30", "ora": "20:30", "luogo del concerto": "Hampden Park, Glasgow", "coordinate geografiche del concerto": "55.8259, -4.2522", "artista": "Lewis Capaldi", "nome album": "Divinely Uninspired to a Hellish Extent", "costo del biglietto standard": 45, "costo del biglietto premium": 180, "ospiti": "Niall Horan"}

# ]
# result = concertiCollection.insert_many(concerti)      #tramite questo pezzo di codice ho inserito nel database i concerti
#print(result.inserted_id)

#######################################################################################################################


def cerca_concerti():
    scelta = input("""inserisci il metodo di ricerca: 
                1 nome dell'artista
                2 nome dell'album
                3 nome dell'ospite
                :""")
    if scelta == "1":
        metodo = input("inserisci il nome dell'" + (Fore.GREEN + Style.BRIGHT + "artista: " + Fore.MAGENTA))
        result = concertiCollection.find({"artista": metodo})      
    elif scelta == "2":
        metodo = input("inserisci il nome dell'"+ (Fore.GREEN + Style.BRIGHT + "album: " + Fore.MAGENTA))
        result = concertiCollection.find({"nome album": metodo})
    elif scelta == "3":
        metodo = input("inserisci il nome dell'"+ (Fore.GREEN + Style.BRIGHT + "artista: " + Fore.MAGENTA))
        result = concertiCollection.find({"ospiti": metodo})
    else:
        print((Fore.RED + Style.BRIGHT + "non esiste un concerto con il parametro specificato" + Style.RESET_ALL))
    for concerti in result:
        print("\n")
        for informazioniConcerto in concerti:
            print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + (str(informazioniConcerto) + Style.RESET_ALL) + ": " + (Fore.CYAN + str(concerti[informazioniConcerto])))

    concertotrovato = result

    domandaAcquisto = input("vuoi comprare il biglietto? y/n: ").strip().lower()
    if domandaAcquisto == "y":

        if "concerti" in locals():
            concertotrovato = concerti


        prezzoBiglietto = input("vuoi comprare il biglietto standard o premium? s/p: " ).strip().lower()
        print(concertotrovato)
        if prezzoBiglietto == "s":
            
            
            prezzo_unitario = concertotrovato.get("costo del biglietto standard", 0)
            quantita = int(input("Quanti biglietti " + (Style.BRIGHT + Fore.CYAN + "standard ") + (Style.RESET_ALL + "vuoi comprare? ") + (Fore.GREEN + Style.BRIGHT)))
            prezzo_totale = prezzo_unitario * quantita
            print(f"Hai acquistato {quantita} biglietti standard per {concertotrovato['artista']} a {prezzo_totale} EUR complessivi.")
        

        elif prezzoBiglietto == "p":
            

            prezzo_unitario = concertotrovato.get("costo del biglietto premium", 0)
            quantita = int(input("Quanti biglietti "+ (Style.BRIGHT + Fore.YELLOW + "premium ") + (Style.RESET_ALL + "vuoi comprare? ") + (Fore.GREEN + Style.BRIGHT)))
            prezzo_totale = prezzo_unitario * quantita
            print(f"Hai acquistato {quantita} biglietti premium per {concertotrovato['artista']} a {prezzo_totale} EUR complessivi.")
        


        else:
            print((Fore.RED + Style.BRIGHT + "error"))
    
    
    
    
    if domandaAcquisto == "n":
        print(Fore.RED + Style.BRIGHT + "grazie per non aver acquistato il biglietto")

cerca_concerti()
