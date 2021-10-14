
import os
import requests

def video_download(url,store_filename):
    data=requests.get(url,stream = True)

    with open(store_filename,'wb') as f:
        for chunk in data.iter_content():
            if chunk: 
                f.write(chunk)
        return store_filename
