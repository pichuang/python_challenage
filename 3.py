__author__ = 'root'

import urllib3
import re
import os


def download(src):
    http = urllib3.PoolManager()
    with http.urlopen('GET', src) as request_data:
        return request_data

# Write file
if not os.path.isfile("3.txt"):
    print("3.txt is not exist")

    # Open connection
    request = download("http://www.pythonchallenge.com/pc/def/equality.html")
    with open("3.txt", "wb") as file:
        file.write(request.data)

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

data = re.findall('([a-z]|\s)[A-Z]{3}([a-z])[A-Z]{3}([a-z]|\s)', read_file)

result = []
for c in data:
    result.append(c[1])
answer = ''.join(result)
print("Answer: {0}".format(answer))
