from tabulate import tabulate

# Código ANSI para vermelho
RED = '\033[31m'
RESET = '\033[0m'

matriz = [
    [1, 2, 3],
    [4, f"{RED}5{RESET}", 6],  # Colorir o '5' de vermelho
    [7, 8, 9]
]

print(tabulate(matriz, tablefmt="fancy_grid"))
