#! python3

import os
import pickle
import datetime
# Gmail API utils
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
# for encoding/decoding messages in base64
from base64 import urlsafe_b64decode, urlsafe_b64encode
# Win10toast imports
from win10toast import ToastNotifier

# Request all access (permission to read/send/receive emails, manage the inbox, and more)
SCOPES = ['https://mail.google.com/']

def gmail_authenticate():
    creds = None
    # the file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time
    if (os.path.exists("token.pickle")):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)
    # if there are no (valid) credentials availablle, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # save the credentials for the next run
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)
    return build('gmail', 'v1', credentials=creds)

def search_emails(service, query):
    result = service.users().messages().list(userId='me', q=query).execute()
    messages = []
    messages.extend(result.get('messages'))
    while 'nextPageToken' in result:
        page_token = result.get('nextPageToken')
        result = service.users().messages().list(userId='me', q=query, pageToken=page_token).execute()
        messages.extend(result.get('messages'))
    
    return messages

def send_toast(service, messages):
    toaster = ToastNotifier()
    most_recent = service.users().messages().get(userId='me', id=messages[0].get('id')).execute()
    most_recent_date = datetime.datetime.fromtimestamp(int(most_recent.get('internalDate')) / 1e3)
    today = datetime.date.today()
    diff = today - most_recent_date.date()
    if diff.days <= 2:
        payload = most_recent.get('payload')
        headers = payload.get('headers')
        headers_sender = [x for x in headers if x.get('name') == 'From']
        headers_subject = [x for x in headers if x.get('name') == 'Subject']
        sender = headers_sender[0].get('value')
        subject = headers_subject[0].get('value')
        toaster.show_toast(f"Nuevo correo: {sender[:23]}...\n{most_recent_date}", f"{subject}", icon_path=None, duration=6)

    return

service = gmail_authenticate()

msgs = search_emails(service, 'google')

send_toast(service, msgs)
