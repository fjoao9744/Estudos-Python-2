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
    
    if len(lista) < 2:
        raise ValueError("A lista deve conter mais de dois itens")
    
    inicio = 0
    fim = len(lista) - 1
    
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == item:
            return meio
        
        elif lista[meio] < item:
            inicio = meio + 1
            
        elif lista[meio] > item:
            fim = meio - 1
            
    return -1
    
lista = [1, 5, 2, 9, 10, 5, 6, 8, 3, 0, -3]

print(lista)
bubble_sort(lista)
print(lista)
print(busca_binaria(lista, 0))