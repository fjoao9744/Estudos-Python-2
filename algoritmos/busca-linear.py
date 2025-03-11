def linear_search(lista, item):
    for i in lista:
        if i == item:
            return lista.index(i)
    else:
        return -1
    
l = [1, 4, 8, 9, 10, 14, 23, 1, 2, 6]

print(linear_search(l, 90))
