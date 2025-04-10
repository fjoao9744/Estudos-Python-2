def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

lista = [100, 30, 40, 20, -3, 0, 9, 0, 40, 50, 5, 6, 2, 3, 4, 5, 1, 2, 0, 90, 60]

print(lista)

bubble_sort(lista)

print(lista)
