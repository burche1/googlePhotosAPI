from pprint import pprint
from init_photo_service import service
import pandas as pd


"""
list method
"""
response = service.mediaItems().list(pageSize=25).execute()

lst_medias = response.get('mediaItems')
nextPageToken = response.get('nextPageToken')

while nextPageToken:
    response = service.mediaItems().list(
        pageSize=25,
        pageToken=nextPageToken
    ).execute()

    lst_medias.extend(response.get('mediaItems'))
    nextPageToken = response.get('nextPageToken')

# on df_media_items we get all the photos available at account
df_media_items = pd.DataFrame(lst_medias)