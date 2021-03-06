from pprint import pprint
from init_photo_service import service
import pandas as pd


"""
search method (by album id)
"""
response_albums_list = service.albums().list().execute()
albums_list = response_albums_list.get('albums')

album_id = next(filter(lambda x: "Teste Frame" in x['title'], albums_list))['id']

request_body = {
    'albumId': album_id,
    'pageSize': 25
}

response_search = service.mediaItems().search(body=request_body).execute()

lstMediaItems = response_search.get('mediaItems')
nextPageToken = response_search.get('nextPageToken')

while nextPageToken:
    request_body['pageToken'] = nextPageToken

    response_search = service.mediaItems().search(body=request_body).execute()
    lstMediaItems.extend(response_search.get('mediaItems'))
    nextPageToken = response_search.get('nextPageToken')

df_search_result = pd.DataFrame(lstMediaItems)
print(df_search_result)
 
 
def response_media_items_by_filter(request_body: dict):
    try:
        response_search = service.mediaItems().search(body=request_body).execute()
        lstMediaItems = response_search.get('mediaItems')
        nextPageToken = response_search.get('nextPageToken')
 
        while nextPageToken:
            request_body['pageToken'] = nextPageToken
            response_search = service.mediaItems().search(body=request_body).execute()
 
            if not response_search.get('mediaItem') is None:
                lstMediaItems.extend(response_search.get('mediaItems'))
                nextPageToken = response_search.get('nextPageToken')
            else:
                nextPageToken = ''
        return lstMediaItems
    except Exception as e:
        print(e)
        return None