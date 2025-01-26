from dataclasses import dataclass

@dataclass # (frozen=True)
class Pessoa:
    nome: str
    idade: int
    
joao = Pessoa("joao", 15)
print(joao)

joao.nome = "josé"
print(joao)
