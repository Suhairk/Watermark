import os
import requests
def image(url,store_filename):
  url_img=requests.get(url)                                                                                               
  with open(store_filename,'wb') as f1:         
    f1.write(url_img.content)
  return store_filename                                              
                                                     

