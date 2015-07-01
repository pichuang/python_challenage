__author__ = 'roan'

import re
import urllib3
import os
import bz2

def download(src):
    http = urllib3.PoolManager()
    request_data = http.urlopen('GET', src)
    request_data.close()
    return request_data

# Write file
if not os.path.isfile("8.txt"):
    print("8.txt is not exist")

    # Open connection
    request = download("http://www.pythonchallenge.com/pc/def/integrity.html")
    with open("8.txt", "wb") as file:
        file.write(request.data)

# Read file
with open("8.txt", "r") as file:
    read_file = file.read()

# Get mess below
data = re.findall('<!--(.+?)-->', read_file, re.S)[-1]
un_data = re.findall('un: \'(.+?)\'', data)
pw_data = re.findall('pw: \'(.+?)\'', data)

un_data = bytearray(un_data)
pw_data = bytearray(pw_data)

un = bz2.BZ2Decompressor().decompress(un_data)
pw = bz2.BZ2Decompressor().decompress(pw_data)

print("{0} {1}".format(un, pw))

