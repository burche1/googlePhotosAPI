from init_photo_service import service
import pandas as pd


response = service.albums().list(
    pageSize=50,
    excludeNonAppCreatedData=False
).execute()
# get's albums information's : id, title, productURL, mediaItensCount, coverPhotoBaseUrl, coverPhotoMediaItemId
 
lstAlbums = response.get('albums')              # same result as response, cause there is no nextPageToken available
nextPageToken = response.get('nextPageToken')   # result is none to my library, cause I have less albuns than the pageSize limit

while nextPageToken:
    response = service.albums().list(
        pageSize=50,
        excludeNonAppCreatedData=False,
        pageToken=nextPageToken
    )
    lstAlbums.append(response.get('albums'))
    nextPageToken = response.get('nextPageToken')

# using pandas to better configure the lstAlbums created
df_albums = pd.DataFrame(lstAlbums)

my_album_id = df_albums[df_albums['title']=='My Family Photos']['id'][3]

# using this my_album_id, get information's about this album
response = service.albums().get(albumId=my_album_id).execute()


"""
Share and unshare methods
"""
request_body = {
    'sharedAlbumOptions': {
        'isCollaborative': True,
        'isCommentable': True
    }
}

response = service.albums().share(
    albumId=my_album_id,
    body=request_body
).execute()
 
service.albums().unshare(albumId=my_album_id).execute()