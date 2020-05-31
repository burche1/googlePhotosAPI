from init_photo_service import service
import pandas as pd

"""
Pandas configuration:

pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 50)
pd.set_option('display.max_colwidth', 32)
pd.set_option('display.width', 120)
pd.set_option('expand_frame_repr', True)
"""
 
"""
list method
"""
response = service.albums().list(
    pageSize=50,
    excludeNonAppCreatedData=False
).execute()
# get's albums information's : id, title, productURL, mediaItensCount, coverPhotoBaseUrl, coverPhotoMediaItemId

print(response)			# print it
print(response.keys())	# the dictionary keys are 'albums' and 'nextPageToken' if available
 
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

print(df_albums)