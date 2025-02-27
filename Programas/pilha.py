from collections import deque

class Stack:
    def __init__(self):
        self.items = deque()
        
    def push(self, item):
        """Adiciona um item na pilha"""
        self.items.append(item)
    
    def pop(self):
        """Remove o ultimo item adicionado na pilha"""
        if not self.is_empty():
            return self.items.pop()
        
        raise IndexError("A pilha esta vazia")
        
    def peek(self):
        """Retorna o elemento do topo"""
        if not self.is_empty():
            return self.items[-1]
        
        raise IndexError("A pilha esta vazia")
    
    def is_empty(self):
        """Verifica se a lista esta vazia"""
        return len(self.items) == 0
        
    def size(self):
        """Retorna o tamanho da pilha"""
        return len(self.items) 
        
        
        