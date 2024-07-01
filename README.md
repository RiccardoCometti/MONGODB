Progetto Gestione Concerti e Biglietti con MongoDB
Questo progetto fornisce un'interfaccia per la gestione dei concerti e l'acquisto di biglietti utilizzando MongoDB come backend.

Requisiti
Python 3.x
pymongo
bson


Installazione
Clona il repository o scarica i file.
Installato le dipendenze richieste eseguendo:
bash
pip install pymongo bson


python
client = MongoClient("mongodb://localhost:27017")

bash
python comandi.py
Segui le istruzioni nel terminale per cercare concerti e acquistare biglietti.

Funzionalità
Cercare Concerti
Puoi cercare concerti in base a tre criteri:

Artista
Album
Ospite

Acquisto Biglietti
Una volta selezionato un concerto, puoi acquistare i biglietti. Il sistema chiede se preferisci acquistare il biglietto premium o standard, calcola il totale e aggiorna il prezzo finale.


il file
dopo gli import e aver stabilito la connessione con mongo db
abbiamo inserito i concerti da python come lista e inseriti in mongo tramite il comando
-result = concertiCollection.insert_many(concerti)-
abbiao creato una funzione unica che permette prima la ricerca tramite i parametri sopracitati il concerto, 
e poi conferisce all'utente di comprare o no i biglietti.
se l'utente desidera acquistare i biglietti il programma chiede se il biglietto desiderato è standard o premium
infine chiede quanti biglietti si desideri comprare e fa il prodotto tra la quantità e il prezzo di un singolo concerto.

####################################################################################################################
Contatti
Per qualsiasi domanda, contatta Riccardo Cometti, Mario Campana, Alessandro Belvedere, Alessandro Fornara.
