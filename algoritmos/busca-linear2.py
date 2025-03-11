def linear_search(lista, item):
    for i in range(len(lista)):
        if lista[i] == item:
            return i
    
    return -1

l = [1, 4, 8, 9, 10, 14, 23, 1, 2, 6]

print(linear_search(l, 23))
