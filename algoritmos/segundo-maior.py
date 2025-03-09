def segundo_maior(arr: list):
    if len(arr) < 2:
        raise ValueError("O array deve conter no minimo 2 numeros")
    
    return sorted(arr)[-2]

print(segundo_maior([3, 5, 1]))

