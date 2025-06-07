from tabulate import tabulate
from InquirerPy.resolver import prompt
import os

matriz = [[0 for _ in range(5)] for _ in range(5)]

def matriz_reset():
    global matriz
    matriz = [[0 for _ in range(5)] for _ in range(5)]

while True:
    print(tabulate(matriz, tablefmt="fancy_grid"))
    
    perguntas = [
        {"type": "list",
        "message": "",
        "choices": ["cima", "baixo", "meio", "diagonal", "diagonal invertida", "meio vertical", "esquerda", "direita", "sair"],
        }
    ]

    resul = prompt(perguntas)

    matriz_reset()

    match resul[0]:
        case "cima":
            for c in range(len(matriz[0])):
                matriz[0][c] = 1
                
        case "baixo":
            for c in range(len(matriz[0])):
                matriz[-1][c] = 1
        
        case "meio":
            for c in range(len(matriz[0])):
                matriz[len(matriz) // 2][c] = 1
                
        case "diagonal":
            for c in range(len(matriz)):
                matriz[c][c] = 1
                
        case "diagonal invertida":
            n = len(matriz)
            for c in range(n):
                matriz[c][n - 1 - c] = 1
            
        case "meio vertical":
            for c in range(len(matriz)):
                matriz[c][len(matriz[0]) // 2] = 1
            
        case "esquerda":
            for c in range(len(matriz)):
                matriz[c][0] = 1
        case "direita":
            for c in range(len(matriz)):
                matriz[c][-1] = 1
        
        case "sair":
            break
        
    os.system("cls")
            