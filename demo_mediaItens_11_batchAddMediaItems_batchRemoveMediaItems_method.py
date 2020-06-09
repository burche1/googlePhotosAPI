from init_photo_service import service
import pandas as pd

"""
batchAddMediaItems & batchRemoveMediaItems
"""

response = service.albums().list(
	pageSize=50,
	excludeNonAppCreatedData=False
).execute()

lstAlbums = response.get('albums')
nextPageToken = response.get('nextPageToken')

while nextPageToken:
	response = service.albums.list(
		pageSize=50,
		excludeNonAppCreatedData=False,
		pageToken=nextPageToken
		
	)
	lstAlbums.append(response.get('albums'))
	nextPageToken = response.get('nextPageToken')

df_albums = pd.DataFrame(lstAlbums)

album_id = df_albums['id'][2]

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

df_media_items = pd.DataFrame(lst_medias)
media_items_ids = df_media_items['id'][:3].to_list()
# only photos uploaded using API could be move

request_body = {
	'mediaItemsIds': media_items_ids
}

response = service.albums().batchAddMediaItems(
	albumId=album_id,
	body=request_body
).execute() 

service.albums().batchRemoveMediaItems(
	albumId=album_id,
	body=request_body
).execute() 
