from pprint import pprint
from init_photo_service import service
import pandas as pd


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

"""
get method
"""
media_id = df_media_items['id'][4923]								# only media ID
response = service.mediaItems().get(mediaItemId=media_id).execute()	# complete media item

print(media_id)
print(response)