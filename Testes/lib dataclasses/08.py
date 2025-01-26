from dataclasses import dataclass, replace

@dataclass
class Pessoa:
    nome: str
    idade: int
    
joao = Pessoa("joao", 15)
new_joao = replace(joao, idade=19)

print(joao) # Pessoa(nome='joao', idade=15)
print(new_joao) # Pessoa(nome='joao', idade=19)


