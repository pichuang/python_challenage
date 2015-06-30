__author__ = 'root'

import urllib3
import os
import re


def download(src):
    http = urllib3.PoolManager()
    request_data = http.urlopen('GET', src)
    request_data.close()
    return request_data

# Write file
if not os.path.isfile("2.txt"):
    print("2.txt is not exist")

    # Open connection
    request = download("http://www.pythonchallenge.com/pc/def/ocr.html")
    with open("2.txt", "wb") as file:
        file.write(request.data)
        file.close()

# Read file
with open("2.txt", "r") as file:
    read_file = file.read()

# Get mess below
data = re.findall('<!--(.+?)-->', read_file, re.S)[-1]

# Count char
counts = {}
for char in data:
    counts[char] = counts.get(char, 0) + 1
print(counts)

# Only print rare char
print("Answer: {0}".format(''.join(re.findall('[a-z]', data))))
