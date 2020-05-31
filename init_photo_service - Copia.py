import os
from Google import Create_Service
import pandas as pd
 
API_NAME = 'photoslibrary'
API_VERSION = 'v1'
CLIENT_SECRET_FILE = 'client_secret_GooglePhotosAPI.json'
SCOPES = ['https://www.googleapis.com/auth/photoslibrary',
          'https://www.googleapis.com/auth/photoslibrary.sharing']
 
service = Create_Service(CLIENT_SECRET_FILE,API_NAME, API_VERSION, SCOPES)  

#ID do cliente:
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

#Chave secreta:
#XXXXXXXXXXXXXXXXXXXXXXXX