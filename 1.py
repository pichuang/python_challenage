__author__ = 'root'

__author__ = 'pichuang'

import string

content = '''
g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
'''

lowercase = string.ascii_lowercase

"""Caser Cipher"""
casesar_cipher = str.maketrans(lowercase, lowercase[2:] + lowercase[:2])
print(lowercase[2:] + lowercase[:2])

""" Content use Caser Cipher"""
print(content.translate(casesar_cipher))

# http://www.pythonchallenge.com/pc/def/map.html
print('map'.translate(casesar_cipher))

