# somar todos os elementos de uma matriz

from random import randint

y = int(input("y: "))
x = int(input("x: "))

matriz = [[randint(0, 9) for _ in range(x)] for _ in range(y)]

c = 0

for line in matriz:
    for i in line:
        c += i

for _ in matriz:
    print(_)
    
print(f"A soma de todos os numeros da matriz é de {c}")