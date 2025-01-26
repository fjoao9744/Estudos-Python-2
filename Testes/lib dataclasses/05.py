from dataclasses import dataclass, field, asdict

@dataclass
class Pessoa:
    nome: str = field(default='')
    idade: int = field(default=0)
    
joao = Pessoa("joao")
joao = asdict(joao)

print(joao)

