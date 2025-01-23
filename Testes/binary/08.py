import struct

num = 19
num = struct.pack("i", num)

print(num)

num = struct.unpack("i", num)

print(num)


