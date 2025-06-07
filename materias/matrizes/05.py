# contar numeros de uma matriz
from random import randint

y = int(input("Digite quantas colunas vão ter na matriz: "))
x = int(input("Digite quantas linhas vão ter na matriz: "))

matriz = [[randint(0, 9) for _ in range(x)]for _ in range(y)]

for _ in matriz:
    print(_)

c = 0
for n1 in matriz:
    for n2 in n1:
        if n2 % 2 == 0:
            c += 1
        
print(f"Foram contados {c} numeros pares na matriz")