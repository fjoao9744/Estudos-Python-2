b1 = b"\x00\x0F"

print(int.from_bytes(b1, "big")) # converte um binario em um inteiro

b2 = 4

print(b2.to_bytes(b2, "big")) # converte um inteiro em um binario

