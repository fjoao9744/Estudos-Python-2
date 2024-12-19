# dataclasses

from dataclasses import dataclass

@dataclass
class Pessoa:
    nome : str
    idade: int
    sexo : str
    
    def apresentar(self):
        print(f"ola, meu nome é {self.nome}")
    
    
jorge = Pessoa("jorge", 12, "M")

print(jorge)
print(jorge.nome)
jorge.apresentar()