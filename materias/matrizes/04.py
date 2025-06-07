# acessando diagonal secundaria /
from random import randint

matriz = [[randint(0, 9) for x in range(10)] for y in range(10)]

for _ in matriz:
    print(_)
    
n = len(matriz)
for c in range(n):
    print(matriz[c][n - 1 - c])