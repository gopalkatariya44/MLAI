from posixpath import split
import string

from pyparsing import Word

_str = 'my name is gopal'

# reversed string
print(_str[::-1])

# split in list
_str1 = _str.split(" ")
print(_str1)

# list to string with
print('-'.join(_str1))

# replace Word
print(_str.replace(' gopal', ' name'))