from collections import deque

llist = deque('abcde') 

print(llist)

llist.extend('fgh') # extend adiciona itens no começo ou no final da llist

print(llist)

llistn = deque(range(0, 10)) # as listas encadeadas tem tipagem estatica
llistn.extendleft([-1, -2])

print(llistn)
