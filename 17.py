__author__ = 'root'

import requests
import re
import bz2
import urllib.parse
import logging
from xmlrpc import client

"""
Log handle
"""
LEVEL = "INFO"
logger = logging.getLogger('17')
logger.setLevel(LEVEL)
console = logging.StreamHandler()
console.setLevel(LEVEL)
logger.addHandler(console)


"""
Handle cookies by level4
"""

ACCOUNT = "huge"
PASSWORD = "file"

src = "http://www.pythonchallenge.com/pc/def/linkedlist.php"
logger.info("Use URL: {0}".format(src))
request_data = requests.get(src, auth=(ACCOUNT, PASSWORD))

# Convert request_data from cookiejar to dict
cookies_dict = requests.utils.dict_from_cookiejar(request_data.cookies)
for key, value in cookies_dict.items():
    logger.info("Got cookies: {0} {1}".format(key, value))


"""
Got "you+should+have+followed+busynothing..." in info from cookies
Change url source to "http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing"
"""

src = "http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=12345"
logger.info("Change url to {0}".format(src))
request_data = requests.get(src, auth=(ACCOUNT, PASSWORD))
logger.info("Got text: {0}\n".format(request_data.text))


"""
Parsing html and got number, cookie
"""

result = []
number = "12345"
src = "http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing={number}".format(number=number)
number_value = re.compile("and the next busynothing is (\d+)")

while True:
    request_data = requests.get(src, auth=(ACCOUNT, PASSWORD))
    cookies_dict = requests.utils.dict_from_cookiejar(request_data.cookies)

    # Add value from cookies
    for key, value in cookies_dict.items():
        logger.info("Got cookie {0}:{1}".format(key, value))
        result.append(value)

    # Get number and change to next page
    try:
        number = number_value.search(request_data.text).group(1)
        logger.debug(number)
    except:
        break

    src = "http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing={number}".format(number=number)

raw_data = ''.join(result)
logger.debug(raw_data)


"""
Python Challenge level 17 in Python 3
    Use the urllib.parse.unquote_to_bytes() function here. It does not support the + to space mapping
    Reference
        -http://stackoverflow.com/questions/29082540/python-challenge-level-17-in-python-3

Test string:
    "BZh91AY%26SY%94%3A%E2I%00%00%21%19%80P%81%11%00%AFg%9E%A0+%00hE%3DM%B5%23%D0%D4%D1%E2%8D%06%A9%FA%26S%D4%D3%21%A1%EAi7h%9B%9A%2B%BF%60%22%C5WX%E1%ADL%80%E8V%3C%C6%A8%DBH%2632%18%A8x%01%08%21%8DS%0B%C8%AF%96KO%CA2%B0%F1%BD%1Du%A0%86%05%92s%B0%92%C4Bc%F1w%24S%85%09%09C%AE%24%90"
"""

# Wrong method: bz2_data = urllib.parse.unquote_to_bytes(urllib.parse.unquote_plus(raw_data))
bz2_data = urllib.parse.unquote_to_bytes(raw_data.replace('+', '%20'))
logger.debug(bz2_data)

bz2decode_data = bz2.decompress(bz2_data).decode('ascii')  # Return str
logger.info("Decoded: {0}".format(bz2decode_data))


"""
Got text: is it the 26th already? call his father and inform him that "the flowers are on their way". he'll understand.
Depends on Level 15, we know Mozart's Father name, Leopold Mozart
Use Level 13 method to call him
"""

phonebook = client.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
logger.info("Mozart's father phone number: {0}".format(phonebook.phone("Leopold")))


"""
Got text: 555-violin, jump to http://www.pythonchallenge.com/pc/stuff/violin.php
Got title name: it's me. what do you want?
Try to send "the flowers are on their way" to him
"""

src = "http://www.pythonchallenge.com/pc/stuff/violin.php"
logger.info("Use URL: {0}".format(src))

# Set cookies info
msg = "the flowers are on their way"
cookies = dict(info=msg)

# Send request to server
request_data = requests.get(src, auth=(ACCOUNT, PASSWORD), cookies=cookies)
logger.info(request_data.text)
