from pprint import pprint
from init_photo_service import service
import pandas as pd


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


"""
search method (feature filter)
"""
request_body = {
    'pageSize': 100,
    'filters': {
        'featureFilter': {
            'includedFeatures': ['FAVORITES']
        }
    }
}
 
df_search_result = pd.DataFrame(response_media_items_by_filter(request_body))
print(df_search_result)