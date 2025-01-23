frase = b"\x00\xFF\x10"

print(int.from_bytes(frase, "big"))

with open("binary.bin", "wb") as b:
    b.write(frase)


