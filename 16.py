__author__ = 'root'

import urllib3
import os
from PIL import Image
from PIL import ImageChops

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

# Download jpg
filename = "16.gif"
url_src = "http://www.pythonchallenge.com/pc/return/mozart.gif"
download_img(filename, url_src)

im = Image.open("16.gif")
im_x, im_y = im.size
magic = 195  # Magic number

DEBUG = False

for y in range(im_y):
    """
    Crop Images with PIL/Pillow
        http://matthiaseisen.com/pp/patterns/p0202/
    """
    box = 0, y, im_x, y+1  # x1, y1, x2, y2: Defined crop size,
    crop_im = im.crop(box)  # Crop all image
    bytes_list = crop_im.tostring()
    if DEBUG:
        print("box:{0} {1}".format(box, bytes_list))  # Print all bytes per line
    position = bytes_list.index(magic)  # Find magic bytes
    if DEBUG:
        print("Position: {0}".format(position))

    """
    From hits, "let me get this straight", so we offset all chr(195) to be a straight line

    ImageChops (Image channel operations): Only Support L and RGB mode (8bits)

    ImageChops.offset(thumb, offset_x, offset_y)
    Returns a new image the same size as the original, but with all pixels rotated dx in the +x direction,and dy in the
    +y direction. If dy is omitted, it defaults to the same value as dx.
    """
    crop_im = ImageChops.offset(crop_im, -position)  # Per line handle
    im.paste(crop_im, box)

im.save("16_answer.gif")
