from collections import deque

llist = deque("acd")

print(llist)

lista = list(llist)

lista.insert(1, 'b')

llist = deque(lista)

print(llist)

