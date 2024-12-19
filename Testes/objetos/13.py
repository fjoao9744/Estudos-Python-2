# dataclasses

from dataclasses import dataclass

@dataclass(order=True)
class Pessoa:
    nome : str
    idade: int
    sexo : str = "I"
    
    def apresentar(self):
        print(f"ola, meu nome é {self.nome}")
        
pessoas = [
    Pessoa("jorge", 12, "M"),
    Pessoa("maria", 18, "F"),
    Pessoa("jose", 16)
           ]

print(pessoas)

for _ in pessoas:
    _.apresentar()


