from dataclasses import dataclass, is_dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int
    
joao = Pessoa("joao", 15)
print(is_dataclass(joao))


