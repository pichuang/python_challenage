__author__ = 'roan'


'''
http://www.pythonchallenge.com/pc/return/cave.jpg
'''

import urllib3
import os
from PIL import Image

ACCOUNT = "huge"
PASSWORD = "file"


def download(src):
    http = urllib3.PoolManager()
    headers = urllib3.util.make_headers(basic_auth='{0}:{1}'.format(ACCOUNT, PASSWORD))
    with http.urlopen('GET', src, headers=headers) as request_data:
        return request_data


# Write file
if not os.path.exists("11.jpg"):
    print("11.jpg is not exist")

    # Open connection
    request = download("http://www.pythonchallenge.com/pc/return/cave.jpg")
    with open("11.jpg", "wb") as file:
        file.write(request.data)

# Open image
im = Image.open("11.jpg")
print(im.size)
size_x, size_y = im.size

"""
Problem: OSError: decoder jpeg not available
Solution (For MAC):
    1. brew install libjpeg libpng
    2. ARCHFLAGS=-Wno-error=unused-command-line-argument-hard-error-in-future pip3 install pillow --allow-external pillow --allow-unverified pillow
Reference:
    http://geekforbrains.com/post/how-to-fix-the-decoder-jpeg-not-available-error-when-using-pil-in-python
"""

for x in range(size_x):
    for y in range(size_y):

        # Print all pixel
        # print(im.getpixel((x, y)))

        # Handle odd pixels
        if (x + y) % 2 == 1:
            # print(im.getpixel((x,y)))
            im.putpixel((x,y), 0 )

im.save("11_new.png", "PNG")
