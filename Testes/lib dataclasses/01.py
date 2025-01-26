# __repr__

from dataclasses import dataclass

@dataclass
class Pessoa1:
    nome: str
    idade: int
    
joao = Pessoa1("joao", 15)

print(joao)


class Pessoa2:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
maria = Pessoa2("maria", 15)

print(maria)

