from random import randint

x = int(input("x: "))
y = int(input("y: "))

matriz = []

for n1 in range(y):
    aux = []
    for n2 in range(x):
        num = randint(1, 9)
        
        if num % 2 == 0:
            aux.append(f"\033[0;32;40m{num}\033[m")
            
        else:
            aux.append(f"\033[0;31;40m{num}\033[m")
            
    matriz.append(aux[:])
    aux.clear()
    
            
for _ in matriz:
    print(' '.join(_))
    
            
        
