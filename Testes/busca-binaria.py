# prototipo

def busca_binaria(lista, item):
    lista.sort()
    
    if len(lista) == 1:
        raise ValueError("A lista deve conter mais de um item")

    i = len(lista) // 2
    i2 = i

    while i:
        if lista[i] == item:
            return i
        
        elif lista[i2] == item:
            return i2
        
        else:
            i += 1
            i2 -= 1

    return -1
          
lista = [12, 40, 5, 6, 9, 10, 32, 90, 1, 80, 6, -4]
lista.sort()

print(lista)
print(busca_binaria(lista, 80))
