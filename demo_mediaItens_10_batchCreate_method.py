import os
import pickle
import requests
from pprint import pprint
from init_photo_service import service
import pandas as pd


"""
batchCretae method
"""
 
# step 1: Upload byte data to Google Server
image_dir = os.path.join(os.getcwd(), 'Imagens para upload')
upload_url = 'https://photoslibrary.googleapis.com/v1/uploads'
token = pickle.load(open('token_photoslibrary_v1.pickle', 'rb'))
 
headers = {
    'Authorization': 'Bearer ' + token.token,
    'Content-type': 'application/octet-stream',
    'X-Goog-Upload-Protocol': 'raw'
}
 
image_file = os.path.join(image_dir, 'imagem_upload_1.jpg')
headers['X-Goog-Upload-File-Name'] = 'Portinari.jpg'
 
img = open(image_file, 'rb').read()
response = requests.post(upload_url, data=img, headers=headers)
print(response) # should be 200
print(response.content) # should be binário token to file
 
request_body  = {
    'newMediaItems': [
        {
            'description': 'Portinari',
            'simpleMediaItem': {
                'uploadToken': response.content.decode('utf-8')
            }
        }
    ]
}
 
upload_response = service.mediaItems().batchCreate(body=request_body).execute()
print(upload_response)  # should be all media item information
message = upload_response.get('newMediaItemResults')[0].get('status')
print(message)          # should be sucess

"""
# Função para batch upload funcionando corretamente

def upload_image(image_path, upload_file_name, token):
    headers = {
        'Authorization': 'Bearer ' + token.token,
        'Content-type': 'application/octet-stream',
        'X-Goog-Upload-Protocol': 'raw',
        'X-Goog-File-Name': upload_file_name
    }    
 
    img = open(image_path, 'rb').read()
    response = requests.post(upload_url, data=img, headers=headers)
    print('#barra n#Upload token: {0}'.format(response.content.decode('utf-8')))
    return response
 
 
tokens = []
image_dir = os.path.join(os.getcwd(), 'Imagens para upload')
upload_url = 'https://photoslibrary.googleapis.com/v1/uploads'
token = pickle.load(open('token_photoslibrary_v1.pickle', 'rb'))
 
image_2 = os.path.join(image_dir, 'imagem_upload_2.jpg')
response = upload_image(image_2, 'Picasso', token)
tokens.append(response.content.decode('utf-8'))
 
image_3 = os.path.join(image_dir, 'imagem_upload_3.jpg')
response = upload_image(image_3, os.path.basename(image_3), token)
tokens.append(response.content.decode('utf-8'))
 
new_media_items = [{'simpleMediaItem': {'uploadToken': tok}}for tok in tokens]
 
request_body = {
    'newMediaItems': new_media_items
}
 
upload_response = service.mediaItems().batchCreate(body=request_body).execute()
"""