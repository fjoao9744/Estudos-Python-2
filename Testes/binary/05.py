b = "héllo".encode("utf-8") # binario

print(b) #b'h\xc3\xa9llo'

c = b.decode("utf-8") # string

print(c) #héllo



