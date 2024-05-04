from flask import Flask, request, jsonify
import datetime
import os

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

app = Flask(__name__)

SCOPES = ['https://www.googleapis.com/auth/calendar']

def authenticate_google_calendar():
    creds = None

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    return build("calendar", "v3", credentials=creds)


@app.route('/create_event', methods=['POST'])
def create_event():
    service = authenticate_google_calendar()

    nome        = "Mario"
    cognome     = "Tomazzolo"
    luogo       = "Segreteria"
    descrizione = "Consegna pagelle"
    giorno      = "9"
    mese        = "5"
    anno        = "2024"
    ora         = "15"
    minuti      = "00"
    durata      = 1

    full_date   = "{}/{}/{}".format(giorno, mese, anno)
    full_time   = "{}:{}".format(ora, minuti)

    start_time  = datetime.datetime.strptime(full_date + "T" + full_time, "%d/%m/%YT%H:%M") + datetime.timedelta(hours=1)
    end_time    = start_time + datetime.timedelta(hours=durata)

    event = {
        'summary': 'Appuntamento di {} {}'.format(nome, cognome),
        'location': luogo,
        'description': descrizione,
        'start': {
            'dateTime': start_time.isoformat(),
            'timeZone': 'Europe/Rome',
        },
        'end': {
            'dateTime': end_time.isoformat(),
            'timeZone': 'Europe/Rome',
        }
    }
    created_event = service.events().insert(calendarId='primary', body=event).execute()
    event_link    = created_event.get('htmlLink')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)