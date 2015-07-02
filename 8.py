__author__ = 'roan'

import re
import urllib3
import os
import bz2

def download(src):
    http = urllib3.PoolManager()
    with http.urlopen('GET', src) as request_data:
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
print("Rawdata: {0}, {1}".format(un_data, pw_data))

# Magic handle
a_data = repr(un_data[0])
b_data = repr(pw_data[0])
print("Repr: {0}, {1}".format(a_data, b_data))


#
# Input string
#
# none replace
#   print(a_data)
#   'BZh91AY&SYA\\xaf\\x82\\r\\x00\\x00\\x01\\x01\\x80\\x02\\xc0\\x02\\x00 \\x00!\\x9ah3M\\x07<]\\xc9\\x14\\xe1BA\\x06\\xbe\\x084'
#
# replace
#   print(a_data.replace("\\\\", "\\"))
#   'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'

a_replace = a_data.replace("\\\\", "\\")
b_replace = b_data.replace("\\\\", "\\")
print("Replace: {0}, {1}".format(a_replace, b_replace))

#
# Hacking string to bytes format
#

un = eval("b" + a_replace)
pw = eval("b" + b_replace)
print("Eval: {0}, {1}".format(un, pw))

# Sample
# un = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
# pw = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

#
# bz2 decompress
#
# un, pw - bytes
# return bytes
#
bytes_un = bz2.decompress(un)
bytes_pw = bz2.decompress(pw)
print("bytes: {0} {1}".format(bytes_un, bytes_pw))

#
# bytes to str
#
str_un = bytes_un.decode("utf-8")
str_pw = bytes_pw.decode("utf-8")
print("str: {0} {1}".format(str_un, str_pw))
