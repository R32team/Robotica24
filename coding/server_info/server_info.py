import socket
import spacy
from transformers import pipeline

# Carica il modello SpaCy italiano
nlp_spacy = spacy.load("it_core_news_sm")

# Inizializza il pipeline di question answering di Hugging Face Transformers
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2", tokenizer="deepset/roberta-base-squad2")

def answer_question(question, context):
    # Analizza la domanda con SpaCy
    doc = nlp_spacy(question)
    
    # Usa il pipeline di QA per trovare la risposta
    qa_result = qa_pipeline({
        'question': question,
        'context': context
    })
    return qa_result['answer']

def server_program():
    host = '0.0.0.0'
    port = 5008

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print("Server in ascolto su {}:{}".format(host, port))

    while True:
        conn, address = server_socket.accept()
        print("Connesso a: ", address)

        question = conn.recv(1024).decode('utf-8')
        if not question:
            break

        # Contesto / testo fornito dallo sviluppatore
        context_text = """La Scuola Cattolica "Alle Stimate" di Verona è un istituto paritario che incorpora vari livelli di istruzione, dalla scuola primaria ai licei, offrendo diversi indirizzi liceali. Fondata nel 1816 da Gaspare Bertoni e gestita dalla Congregazione degli Stimmatini, questa scuola si pone come un punto di riferimento educativo nella comunità di Verona, avendo circa 900 studenti e un corpo docente di circa settanta insegnanti.
Il preside della scuola, insieme al direttore, gioca un ruolo cruciale nella gestione dell'istituto, concentrandosi sugli aspetti didattici e pedagogici. Mentre il preside si occupa prevalentemente della parte educativa e formativa, assicurando la qualità dell'insegnamento e il rispetto dei programmi scolastici, il direttore si focalizza maggiormente sulle questioni amministrative e organizzative, rappresentando l'ente gestore.
La visione educativa della scuola mira a formare studenti responsabili, liberi e consapevoli, promuovendo una visione cristiana come chiave di lettura della realtà. Questo approccio si riflette nel curriculum offerto, che abbraccia una vasta gamma di discipline, integrando tradizione e innovazione e preparando gli studenti a interagire con le diverse culture del mondo contemporaneo.
La scuola si impegna a offrire un'educazione che sviluppa non solo la conoscenza accademica ma anche i valori morali, incentivando gli studenti a diventare individui pensanti, critici e attivi nella società. L'istituto si distingue per il suo ambiente accogliente e per l'attenzione alla crescita personale e spirituale degli studenti, nel rispetto dei valori umanistici cristiani.
"""

        # Trova la risposta
        answer = answer_question(question, context_text)

        # Invia la risposta al client
        conn.sendall(answer.encode('utf-8'))
        conn.close()

# Avvia il server
server_program()
