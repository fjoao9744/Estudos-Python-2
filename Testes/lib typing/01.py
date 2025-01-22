from typing import List

def soma(numeros: List[int]) -> int:
    return sum(numeros)

n: int = soma([2, 3, 10, 5, 5])

print(n, type(n))