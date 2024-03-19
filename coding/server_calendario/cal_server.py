from flask import Flask, request, jsonify
import datetime
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
import os

app = Flask(__name__)

SCOPES = ['https://www.googleapis.com/auth/calendar']
credentials = None

def authenticate_google_calendar():
    global credentials
    credentials_json = {
        "installed": {
            "client_id": "357674996162-pfi2hb7mu2h60se96ip0m1apg601sv02.apps.googleusercontent.com",
            "project_id": "calendario-nao",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_secret": "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",
            "redirect_uris": ["urn:ietf:wg:oauth:2.0:oob", "http://localhost"]
        }
    }

    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            credentials = pickle.load(token)

    if not credentials or not credentials.valid:
        flow = InstalledAppFlow.from_client_config(credentials_json, SCOPES)
        credentials = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(credentials, token)

    return build('calendar', 'v3', credentials=credentials)

@app.route('/create_event', methods=['POST'])
def create_event():
    data = request.json
    nome = data['name']
    cognome = data['surname']
    date = data['date']
    ora = data['time']

    service = authenticate_google_calendar()
    full_date = "{}/2024".format(date)
    start_time = datetime.datetime.strptime(full_date + ' ' + ora, '%d/%m/%Y %H:%M')
    end_time = start_time + datetime.timedelta(hours=1)

    event = {
        'summary': 'Appuntamento di {} {}'.format(nome, cognome),
        'start': {'dateTime': start_time.isoformat(), 'timeZone': 'Europe/Rome'},
        'end': {'dateTime': end_time.isoformat(), 'timeZone': 'Europe/Rome'},
    }

    created_event = service.events().insert(calendarId='primary', body=event).execute()

    return jsonify({"message": "Evento creato con successo", "eventLink": created_event.get('htmlLink')})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
