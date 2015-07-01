__author__ = 'roan'


# http://www.pythonchallenge.com/pc/def/oxygen.png
import os
from PIL import Image
import urllib3
import time


def download(src):
    http = urllib3.PoolManager()
    request_data = http.urlopen('GET', src)
    request_data.close()
    return request_data

# Check zipfile
if not os.path.isfile("7.png"):
    print("7.png is not exist")

    # Open connection
    request = download("http://www.pythonchallenge.com/pc/def/oxygen.png")
    with open("7.png", "wb") as file:
        file.write(request.data)
        file.close()

# Open image
im = Image.open('7.png')
weight, height = im.size
print("weight:{0} height:{1}".format(weight, height))


# Convert tuple to char and display it
print("1 ===")
for x in range(1, 10):  # x - interval
    listx_string = []
    listy_string = []
    listz_string = []
    for i in range(0, weight, x):
        point = im.getpixel((i, height//2))  # Return tuple
        listx_string.append(chr(point[0]))
        listy_string.append(chr(point[1]))
        listz_string.append(chr(point[2]))

    # Compare performance between loop and map
    tStart_loop = time.time()
    print(''.join(str(e) for e in listx_string))  # Use for loop
    tStop_loop = time.time()
    print(''.join(map(str, listy_string)))  # Use map
    tStop_map = time.time()
    print(''.join(map(str, listz_string)))
    print('Use Loop: {0}'.format(tStop_loop - tStart_loop))
    print('Use Map: {0}'.format(tStop_map - tStop_loop))

    if x == 9:
        print()
    else:
        print("{0} {1}".format(x+1, "=" * len(listx_string)))

#  interval = 7 is right answer
# print("Answer: {0}".format(''.join(chr(e) for e in [105, 110, 116, 101, 103, 114, 105, 116, 121])))  # Use for loop
print("Answer: {0}".format(''.join(map(chr, [105, 110, 116, 101, 103, 114, 105, 116, 121]))))  # Use map
