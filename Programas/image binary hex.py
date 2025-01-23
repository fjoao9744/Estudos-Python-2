
with open("dog.jpg", "rb") as dog: # carrega o codigo binairo de uma imagem
    
    dog = dog.read(16) # lê apenas o cabeçario
    
    
print(dog.hex().encode("utf-8")) # mostra o codigo hexadecimal do cabeçario
    
    
    
    

