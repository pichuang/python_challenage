__author__ = 'roan'


'''
http://www.pythonchallenge.com/pc/return/cave.jpg
'''

import urllib3
import os
from PIL import Image

def download(src):
    http = urllib3.PoolManager()
    request_data = http.urlopen('GET', src)
    request_data.close()
    return request_data

# Write file
if not os.path.isfile("11.jpg"):
    print("11.jpg is not exist")

    # Open connection
    request = download("http://www.pythonchallenge.com/pc/return/cave.jpg")
    with open("11.jpg", "wb") as file:
        file.write(request.data)

# Open image
im = Image.open('11.jpg')
