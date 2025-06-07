# criação de uma matriz

y = int(input("Digite a quantidade de colunas que a matriz vai ter: "))
x = int(input("Digite a quantidade de linhas que a matriz vai ter: "))

matriz = []

for colunm in range(y):
    line_aux = []
    for line in range(x):
        num = int(input(f"Digite um numero na posição {colunm} {line}:"))
        line_aux.append(num)
        
    matriz.append(line_aux[:])
    line_aux.clear()
    
print(matriz)