# __dict__

class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

jorge = Pessoa("jorge", 18)

print(jorge.__dict__)

jorge.__dict__["idade"] = 13 

print(jorge.__dict__)


