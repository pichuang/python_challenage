__author__ = 'roan'


import urllib3
import os


ACCOUNT = "huge"
PASSWORD = "file"


def download(src):
    http = urllib3.PoolManager()
    headers = urllib3.util.make_headers(basic_auth='{0}:{1}'.format(ACCOUNT, PASSWORD))
    with http.urlopen('GET', src, headers=headers) as request_data:
        return request_data


def download_img(new_name, src):
    if not os.path.exists(new_name):
        # print("{0} is not exist".format(new_name))
        request = download(src)
        with open(new_name, "wb") as file:
            file.write(request.data)

# Download all jpg
for i in range(1, 4):
    filename = "12_" + str(i) + ".jpg"
    url_src = "http://www.pythonchallenge.com/pc/return/evil" + str(i) + ".jpg"
    download_img(filename, url_src)

# Download evil2.gfx by evil2 picture
if not os.path.exists("12.gfx"):
    request = download("http://www.pythonchallenge.com/pc/return/evil2.gfx")
    with open("12.gfx", "wb") as file:
        file.write(request.data)

# Read binary from file
with open("12.gfx", "rb") as buf:
    # Follow png format
    # http://www.libpng.org/pub/png/spec/1.2/PNG-Rationale.html#R.PNG-file-signature
    # hex: 89  50  4e  47  0d  0a  1a  0a

    # Display trunk per 100 bytes
    # for i in range(0, 5): # 5 is a magic number
    #     trunk = buf.read(100)
    #     print(trunk[i::5])
    #     buf.seek(0)  # Reset position

    # 5 picture
    types = ['jpg', 'png', 'gif', 'png', 'jpg']
    for i in range(5):
        with open('12_answer_{0}.{1}'.format(i, types[i]), 'wb') as answer:
            trunk = buf.read(-1)  # Read all buffer
            answer.write(trunk[i::5])  # Split bytes per 5
            buf.seek(0)  # Reset position
