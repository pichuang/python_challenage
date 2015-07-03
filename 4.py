__author__ = 'root'

import requests
import re


ACCOUNT = "huge"
PASSWORD = "file"


def next_page(num):
    src = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={number}".format(number=num)
    request_data = requests.get(src, auth=(ACCOUNT, PASSWORD))
    return request_data


def get_number(data):
    number_value = re.compile("and the next nothing is (\d+)")
    number = number_value.search(data.text).group(1)
    return number


print("Phase 1")
number = "12345"
while True:
    # Get number and change to next page
    request_data = next_page(number)
    try:
        number = get_number(request_data)
        print("Got number {0}".format(number))
    except:
        break
print(next_page(number).text)  # Yes. Divide by two and keep going


print("Phase 2")
number = int(number)  # str to int
number //= 2  # 8022 = 16044 // 2

while True:
    request_data = next_page(number)
    try:
        number = get_number(request_data)
        print("Got number {0}".format(number))
    except:
        break
print("Answer: {0}".format(next_page(number).text))  # peak.html
