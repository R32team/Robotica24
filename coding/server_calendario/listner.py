from flask import Flask, request, jsonify
import subprocess
import threading

app = Flask(__name__)

def start_additional_functionality():
    """
    Questa funzione può avviare un server aggiuntivo, eseguire uno script, o qualsiasi
    operazione desideri quando viene attivata.
    """
    # Esempio: Esegue uno script Python. Sostituisci 'path/to/your_script.py' con il percorso effettivo.
    # subprocess.run(["python", "path/to/your_script.py"])

    print("Server/Script addizionale avviato!")

@app.route('/trigger', methods=['POST'])
def handle_request():
    # Riceve i dati JSON dalla richiesta POST
    data = request.json

    print("Dati ricevuti:", data)

    # Avvia la funzionalità aggiuntiva in un nuovo thread per non bloccare la risposta
    threading.Thread(target=start_additional_functionality).start()

    # Invia una risposta di conferma al client che ha effettuato la richiesta
    return jsonify({"message": "Richiesta ricevuta, azione in esecuzione."})

if __name__ == '__main__':
    # Avvia il server Flask in ascolto su tutte le interfacce disponibili sulla porta 5000
    app.run(host='0.0.0.0', port=5001)
