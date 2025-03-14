def bubble_sort(lista):
    lista = lista
    flag = True
    while flag:
        flag = False
    
        for i in range(len(lista) - 1):
            if lista[i] > lista[i + 1]:
                lista[i + 1], lista[i] = lista[i], lista[i + 1]

                flag = True
                
            else:
                i += 1
    
    return lista

l = [5, 3, 8, 4, 2]
print(l)
print(bubble_sort(l))
