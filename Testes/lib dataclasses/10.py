from dataclasses import dataclass

@dataclass(frozen=True)
class Pessoa2:
    nome: str
    idade: int
    sexo: str
    
p = Pessoa2("joao", 20, "M")

# p.nome = "maria" #erro