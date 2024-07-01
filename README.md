Progetto Gestione Concerti e Biglietti con MongoDB
Questo progetto fornisce un'interfaccia per la gestione dei concerti e l'acquisto di biglietti utilizzando MongoDB come backend.

Requisiti
Python 3.x
pymongo
bson


Installazione
Clona il repository o scarica i file.
Installa le dipendenze richieste eseguendo:
bash
Copia codice
pip install pymongo bson


Configurazione
Assicurati di avere un cluster MongoDB configurato. Sostituisci l'URI di connessione con il tuo URI MongoDB nel file comandi.py:

python
Copia codice
uri = "mongodb+srv://<username>:<password>@<cluster>.mongodb.net/"
Utilizzo
Esegui il file comandi.py:

bash
Copia codice
python comandi.py
Segui le istruzioni nel terminale per cercare concerti e acquistare biglietti.

Funzionalità
Cercare Concerti
Puoi cercare concerti in base a tre criteri:

Artista
Album
Ospite
Acquistare Biglietti
Una volta selezionato un concerto, puoi acquistare i biglietti. Il sistema verifica la disponibilità, calcola il totale e aggiorna la disponibilità dei biglietti nel database.

Esempio di Output
markdown
Copia codice
Per cercare il concerto in base a:
1. Artista
2. Album
3. Ospite
Inserisci il numero corrispondente alla tua scelta e segui le istruzioni successive.

Struttura del Progetto
comandi.py: Il file principale che contiene tutte le funzioni per cercare concerti e acquistare biglietti.
Concerti: Collezione MongoDB che contiene le informazioni sui concerti.
Biglietti: Collezione MongoDB che contiene i biglietti acquistati.
Note
Assicurati di avere le collezioni Concerti e Biglietti nel tuo database Esame_MONGO_DB.
La connessione a MongoDB utilizza l'API Server v1.


Contatti
Per qualsiasi domanda, contatta Riccardo Cometti, Mario Campana, Alessandro Belvedere, Alessandro Fornara.
