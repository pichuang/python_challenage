__author__ = 'roan'


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


def download_img(new_name, src):
    if not os.path.exists(new_name):
        # print("{0} is not exist".format(new_name))
        request = download(src)
        with open(new_name, "wb") as file:
            file.write(request.data)

# Download jpg
filename = "14.png"
url_src = "http://www.pythonchallenge.com/pc/return/wire.png"
download_img(filename, url_src)


#########
        #
######  #
#   ##  #
#       #
#########

wire = Image.open("14.png", "r")
im = Image.new("RGB", (100, 100))  # We know 100*100 from web source
