from __future__ import print_function
import httplib2
import os

from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

import base64
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import mimetypes
import os

from apiclient import errors

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None


SCOPES = 'https://mail.google.com/'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Gmail API Python Quickstart'


def get_credentials():
    

    store = oauth2client.file.Storage('credent.data')
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: 
            credentials = tools.run(flow, store)
        #print('Storing credentials to ' + credential_path)
    return credentials

def main():
    
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)
    message = MIMEText('hello madam ,  teacher of JIIT')
    message['to'] = 'vishal.bisht13104751@gmail.com'
    message['from'] = 'vishal.bisht13104751@gmail.com'
    message['subject'] = 'testing for neetu sardana'

    messages = (service.users().messages().send(userId='me', body={'raw':base64.b64encode(message.as_string())}).execute())
    print (messages['id'])


if __name__ == '__main__':
    main()
