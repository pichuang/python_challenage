__author__ = 'root'

import urllib3
import os
import pickle

def download(src):
    http = urllib3.PoolManager()
    request_data = http.urlopen('GET', src)
    request_data.close()
    return request_data

if not os.path.isfile("5.txt"):
    print("5.txt is not exist")

    # Open connection
    request = download("http://www.pythonchallenge.com/pc/def/banner.p")
    with open("5.txt", "wb") as file:
        file.write(request.data)
        file.close()

# Read file
with open("5.txt", "r") as file:
    read_file = file.read()

data = pickle.loads(read_file)

for list in data:
    print(''.join(t[0] * t[1] for t in list))

file.close()
