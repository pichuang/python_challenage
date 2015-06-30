__author__ = 'root'


import urllib3
import re


def download(num):
    http = urllib3.PoolManager()
    src = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + str(num)
    request_data = http.urlopen('GET', src)
    request_data.close()
    return request_data


def parse(web_str):
    num = ''.join(re.findall(r'and the next nothing is (\d+)', web_str))
    if not num:
        print(web_str)
        exit(0)
    return num


def next_page(num):
    num = parse(download(number).data)
    return num

# First number
# number = 12345

# Yes. Divide by two and keep going
# number =16044

# 8022 = 16044 // 2
number = 8022
i = 0
while True:
    number = next_page(number)
    i += 1
    print("{0} {1}".format(i, number))
