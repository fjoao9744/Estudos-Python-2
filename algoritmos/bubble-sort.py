def bubble_sort(lista):
    lista = lista
    flag = True
    while flag:
        i = aux = 0
        flag = False
    
        while i < len(lista) - 1:
            if lista[i] > lista[i + 1]:
                aux = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = aux
                flag = True
                
            else:
                i += 1
    
    return lista

l = [5, 3, 8, 4, 2]
print(l)
print(bubble_sort(l))
