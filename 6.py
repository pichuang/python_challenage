__author__ = 'roan'

import urllib3
import os
import zipfile
import re


def download(src):
    http = urllib3.PoolManager()
    with http.urlopen('GET', src) as request_data:
        return request_data

# Check zipfile
if not os.path.isfile("6.zip"):
    print("6.zip is not exist")

    # Open connection
    request = download("http://www.pythonchallenge.com/pc/def/channel.zip")
    with open("6.zip", "wb") as file:
        file.write(request.data)

# Check dir
if not os.path.isdir("6"):
    print("6.zip is not extract to be directory")
    with zipfile.ZipFile('6.zip', 'r') as z:
        z.extractall("./6/")


def next_file(num):
    filename = "./6/" + str(num) + ".txt"
    with open(filename, "r") as file:
        read_file = file.read()
        num = re.findall('Next nothing is ([0-9]+)', read_file)
        if not num:
            print(read_file)
            return False  # Return type: Boolean
        else:
            return num  # Return type: List

num = 90052  # First number from readme.txt
num_list = []  # Collect the number list for comment
while True:
    # Check get False or not
    if not num:
        break

    # Covert list to int
    if not isinstance(num, int):
        num = int(''.join(map(str, num)))

    # Append number to num_list
    num_list.append(num)

    # Next run
    num = next_file(num)

result = []
with zipfile.ZipFile('6.zip', 'r') as z:
    for point in num_list:
        # Print comment per specific file
        result.append(z.getinfo('{0}.txt'.format(point)).comment)

# Combine list and print answer

print(b''.join(result).decode("utf-8"))
