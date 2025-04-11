# incompleto

def merge_sort(lista):
    meio = len(lista) // 2
    esquerda = lista[:meio]
    direita = lista[meio:]
    if len(esquerda) > 1:
        merge_sort(esquerda)
        merge_sort(direita)

    print(esquerda, direita)
    print(lista)

lista = [100, 0, -2, 3, 4, 5, 12, 4, -90, -40, 45, 23, 12, -5, 2, 4]

merge_sort(lista)

