from typing import Callable

def executar(func: Callable[[int, int], int], x: int, y: int) -> int: # o terceiro int é o return
    return func(x, y)

def soma(a: int, b: int) -> int:
    return a + b

print(executar(soma, 2, 3))


