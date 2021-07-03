#the struct module in python is used to convert native python data types such as strings and numbers into a string of bytes and vice versa
from struct import *

packed_data=pack('iif',5,7,6.38)
print(packed_data)

print(calcsize('i'))
print(calcsize('f'))
print(calcsize('iif'))

unpacked_data=unpack("iif",packed_data)
print(unpacked_data)

print(unpack('iif',b'\x05\x00\x00\x00\x07\x00\x00\x00\xf6(\xcc@'))
