import os
from Google import Create_Service
import pandas as pd # pip install pandas
import requests # pip install requests
from init_photo_service import service
 
pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 150)
pd.set_option('display.max_colwidth', 150)
pd.set_option('display.width', 150)
pd.set_option('expand_frame_repr', True)

myAblums = service.albums().list().execute()
myAblums_list = myAblums.get('albums')
dfAlbums = pd.DataFrame(myAblums_list)
Teste_Frame_album_id = dfAlbums[dfAlbums['title'] == 'Teste Frame']['id'].to_string(index=False).strip()
 
def download_file(url:str, destination_folder:str, file_name:str):
    response = requests.get(url)
    if response.status_code == 200:
        print('Downloading file {0}'.format(file_name))
        with open(os.path.join(destination_folder, file_name), 'wb') as f:
            f.write(response.content)
            f.close()
 
media_files = service.mediaItems().search(body={'albumId': Teste_Frame_album_id}).execute()['mediaItems']
 
destination_folder = r'/home/pi/Documents/Photos'
 
for media_file in media_files:
    file_name = media_file['filename']
    download_url = media_file['baseUrl'] + '=d'
    download_file(download_url, destination_folder, file_name)

#home/pi/Documents/Photos
