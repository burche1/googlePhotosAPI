from init_photo_service import service
import pandas as pd

"""
create method
"""
request_body = {
    'album': {'title': 'My Family Photos'}
}
# uses the request body above to create an album with the name 'My Family Photos'
response_album_family_photos = service.albums().create(body=request_body).execute()