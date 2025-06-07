# transpor uma matriz

from random import randint

y = int(input("Y: "))
x = int(input("X: "))

matriz = [[randint(0, 10) for _ in range(x)] for _ in range(y)]

def transpor():
    global matriz
    
    new_matriz = []
    
    for i in range(len(matriz[0])):
        aux = []
    
        for line in matriz:
            aux.append(line[i])
            
        new_matriz.append(aux[:])
        aux.clear()
            
    matriz = new_matriz

while True:
    for c in matriz:
        print(c)
        
    op = input("Transpor")
    
    if op == "0":
        break
    
    transpor()
    
        
    
