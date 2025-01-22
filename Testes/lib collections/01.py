from collections import deque

llist = deque() # cria uma lista encadeada vazia

llist.appendleft("a") # appendleft é um metodo apenas do collections
llist.appendleft("b") # esta adicionando um elemento no inicio da llit(linked list)

llist.popleft() # tira um item da llist

print(llist)

