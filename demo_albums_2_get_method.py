from init_photo_service import service
import pandas as pd

"""
list method
"""
response = service.albums().list(
    pageSize=50,
    excludeNonAppCreatedData=False
).execute()
# get's albums information's : id, title, productURL, mediaItensCount, coverPhotoBaseUrl, coverPhotoMediaItemId
 
lstAlbums = response.get('albums')				# same result as response, cause there is no nextPageToken available
nextPageToken = response.get('nextPageToken')	# result is none to my library, cause I have less albuns than the pageSize limit

# if there is more albuns than the pageSize limit, iteration is necessary to get all albums
while nextPageToken:
    response = service.albums().list(
        pageSize=50,
        excludeNonAppCreatedData=False,
        pageToken=nextPageToken
    )
    lstAlbums.append(response.get('ablums'))
    nextPageToken = response.get('nextPageToken')

# using pandas to better configure the lstAlbums created
df_albums = pd.DataFrame(lstAlbums)


"""
get method
"""
# from df_albums get album id for position 0
# AKhXrXYzSAJetq0Xu2zZt2g0gKDzoQog_Y642czKeLiJ1x...
my_album_id = df_albums[df_albums['title']=='Teste Frame']['id'][0]
print(my_album_id)
# using this my_album_id, get information's about this album
response = service.albums().get(albumId=my_album_id).execute()
print(response)