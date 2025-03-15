# solução falha

def bubble_sort(lista):
    while True:
        trocou = False
        for c in range(len(lista) - 1):
            if lista[c] > lista[c + 1]:
                lista[c], lista[c + 1] = lista[c + 1], lista[c]
                trocou = True
                
        if not trocou:
            break
            
def busca_binaria(lista, item):
    
    if len(lista) == 1 or len(lista) == 0:
        raise ValueError("A lista deve conter mais de dois itens")
    
    i1 = len(lista) // 2
    i2 = i1
    
    while i1 < len(lista) and i2 > 0:
        if lista[i1] == item:
            return i1
        
        elif lista[i2] == item:
            return i2
        
        else:
            i1 += 1
            i2 -= 1
            
    return -1
    
lista = [1, 5, 2, 9, 10, 5, 6, 8, 3, 0, -3]

print(lista)
bubble_sort(lista)
print(lista)
print(busca_binaria(lista, -8))