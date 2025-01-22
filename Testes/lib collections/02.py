from collections import deque

llist = deque('abcde') 
print(llist)

llist.rotate() 

print(llist)

llist.rotate(-1)

print(llist)