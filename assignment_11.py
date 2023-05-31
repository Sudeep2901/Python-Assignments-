# String Methods
_str = "I am Learning Python full stack at Cyber Success. With Version of Python 3"
_nstr = '8412046856'
_astr = "G\tO\tO\tD"

#Length : To access string at any index
print(f"First Words of string are : {_str[0:4]}")

#upper case : To make all string alphabets/letters in capital case
print("upper Method : ",_str.upper())

#lower case : To make all string alphabets/letters in small case
print("lower Method : ",_str.lower())

#capitalize (Case) method : To make only first character of string capital
print("capitalize Method : ",_str.capitalize())

#casefold (case) method : To make all string characters in small case but it is less aggressive
print("casefold Method : ",_str.casefold())

#strip : It removes spaces from starting and ending in a string
print("strip Method : ",_str.strip())

#isdigit : checks whether enters string is numbers (zero alphabet tolerance)
print("isdigit Method : ",_nstr.isdigit())

#center : To allign string by center
print(_str.center(10,"*"))

#count : To count number of same words in a string
print("count Method : ",_str.count("Python"))

#encode/decode : Encryption and decryption of string
import base64
_enc = base64.b64encode(bytes('String to be encoded','utf8'))
print("Encoded with base 64 : ",_enc)
_dec = base64.b64decode(_enc)
print("Decoded With base 64 : ",_dec)

#startswith : To check whether a string starts with particular characters
print("startswith Method : ",_str.startswith("I"))

#endswith : To check whether a string ends with particular characters
print("endswith Method : ",_str.endswith("3"))

#expandtabs : To expand tabs \t from 4 to custom
print("expandtabs Method : ",_astr.expandtabs(4))

#find : To find a word in a string (o/p shows index)
print("find Method : ", _str.find("Python"))

#replace : To replace words in a string
print("replace Method : ",_str.replace("Python","CPP"))


#swapcase : changes capital letters to small and small letters to capital
print(f"swapcase method : ",_str.swapcase())