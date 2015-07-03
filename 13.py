__author__ = 'roan'


"""
http://www.pythonchallenge.com/pc/phonebook.php
Use xmlrpc
"""

from xmlrpc import client


phonebook = client.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')

# List phonebook method
print(phonebook.system.listMethods())

method = phonebook.system.listMethods()[0]

print(phonebook.system.methodHelp(method))
print(phonebook.system.methodSignature(method))
print(phonebook.phone("Bert"))  # "Bert is evil", depends on level 12
