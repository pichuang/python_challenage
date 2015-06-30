__author__ = 'root'

import urllib3
import re
import os


def download(src):
    http = urllib3.PoolManager()
    request_data = http.urlopen('GET', src)
    request_data.close()
    return request_data

# Write file
if not os.path.isfile("3.txt"):
    print("3.txt is not exist")

    # Open connection
    request = download("http://www.pythonchallenge.com/pc/def/equality.html")
    with open("3.txt", "wb") as file:
        file.write(request.data)
        file.close()

# Read file
with open("3.txt", "r") as file:
    read_file = file.read()

# One small letter, surrounded by EXACTLY three big bodyguards on each of its sides.
"""
qIQNlQSLi
eOEKiVEYj
aZADnMCZq
bZUTkLYNg
uCNDeHSBj
kOIXdKBFh
dXJVlGZVm
gZAGiLQZx
vCJAsACFl
qKWGtIDCj
"""
data = re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', read_file)
print("Answer: {0}".format(''.join(data)))