from dataclasses import dataclass

@dataclass
class Pessoa:
    # __init__
    nome: str
    idade: int
    
    def __post_init__(self): # o init não funciona pois o init ja foi declarado
        if self.idade < 0:
            raise ValueError("A idade não pode ser negativa.")

j = Pessoa("joao", -1)

