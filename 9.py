__author__ = 'roan'

import urllib3
import os
import re
import turtle


# From challenge 8
ACCOUNT = "huge"
PASSWORD = "file"


def convert_to_list(pattern, content):
    """
    1. match pattern for content
    2. covert to string
    3. replace \n in string
    4. split string by ','
    5. return List(first)
    """
    temp = re.findall(pattern, content)
    ll = ''.join(temp).replace('\n', '').split(',')
    return ll


def download(src):
    http = urllib3.PoolManager()
    headers = urllib3.util.make_headers(basic_auth='{0}:{1}'.format(ACCOUNT, PASSWORD))
    with http.urlopen('GET', src, headers=headers) as request_data:
        return request_data

if not os.path.isfile("9.txt"):
    print("9.txt is not exist")

    # Open connection
    request = download("http://www.pythonchallenge.com/pc/return/good.html")
    with open("9.txt", "wb") as file:
        file.write(request.data)

# Read file
with open("9.txt", "r") as file:
    read_file = file.read()


'''
Regular expression
'''
clean_page = re.findall('<!--((?:[^-]+|-[^-]|--[^>])*)-->', read_file)[1]
# print(clean_page)

first = convert_to_list('first:(\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*)', clean_page)
# print(first)

second = convert_to_list('second:(\n.*\n.*\n.*\n.*\n.*)', clean_page)
# print(second)

'''
Build x-y plane list from first and second
'''
# [x0, y0, x1, y1, ...]
first_zip_list = list(map(list, zip(first[0::2], first[1::2])))  # map(list, tuple)
# print(first_zip_list)

second_zip_list = list(map(list, zip(second[0::2], second[1::2])))
# print(second_zip_list)

# First + second
first_zip_list.extend(second_zip_list)

'''
Drawing
'''
wn = turtle.Screen()
alex = turtle.Turtle()
alex.speed(0)
alex.resizemode("auto")
alex.degrees(270)
for x, y in first_zip_list:
    alex.setpos(int(x), int(y))
wn.mainloop()
