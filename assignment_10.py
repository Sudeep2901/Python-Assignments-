#Program to compress and decompress a string with bz2 module

_title = "******Program To Encode and Decode using bz2******"
#_title.center(50,"*")
print(_title)
import bz2  #Module
#_str = b'Learning Python at Cyber Success'
_str = bytes(input("Enter a string : "),'utf-8')
_compress = bz2.compress(_str)  #encoding
print(f"Encoded String is : {_compress}")
_decompress = bz2.decompress(_compress) #decoding
print(f"Decoded String is : {_decompress}")