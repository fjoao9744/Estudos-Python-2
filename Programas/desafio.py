from itertools import permutations

def cript(data):
    """Calcula todas as somas possíveis dos dígitos do número"""
    digits = set()

    for c in range(len(data)):    
        for num in data:
            digits.add(data[c] + num)  # Soma os valores do número
    
    return digits

def descript(valid_set, size):
    """Encontra os números possíveis que geram o conjunto de somas"""
    digitos_possiveis = [0, 2, 4, 6, 8]  # Apenas números pares

    resultados = set()
    
    for comb in permutations(digitos_possiveis, size):
        sdata = list(comb)  # A tupla de permutação é transformada em lista

        # Compara a soma das permutações com o conjunto válido
        if cript(sdata) == valid_set:
            numero = "".join(map(str, comb))  # Junta os dígitos em uma string
            resultados.add(numero)  # Adiciona ao conjunto de resultados
    
    return resultados

# Testa as funções
print(cript([2, 0, 0, 4]))  # Esperado: {0, 2, 4, 6, 8}
print(descript(cript([2, 0, 0, 4]), 4))  # Encontra as permutações que geram o conjunto esperado
