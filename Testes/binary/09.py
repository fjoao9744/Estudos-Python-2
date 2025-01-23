import struct

with open("binary.bin", "rb") as b:
    numbyte = b.read()
    num = struct.pack("i", int.from_bytes(numbyte))

print(num)
print(struct.calcsize("i"))


