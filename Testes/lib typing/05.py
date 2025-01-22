from typing import List, Tuple, Dict

def pares(numeros: List[int]) -> Dict[int, Tuple[int, int]]:
        return {num: (num, num * -1) for num in numeros}
    
print(pares([3, 5, 10]))

