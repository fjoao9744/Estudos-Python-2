# criação de uma matriz

y = int(input("Digite a quantidade de colunas que a matriz vai ter: "))
x = int(input("Digite a quantidade de linhas que a matriz vai ter: "))

matriz = [input().split() for colunm in range(y)]

print(matriz)