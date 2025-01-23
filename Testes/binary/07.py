import struct

num = struct.pack("i", 1024)

print(num)

unpacked = struct.unpack("i", num)

print(unpacked)


import sys

print(sys.getsizeof(1024))
print(sys.getsizeof(num))
