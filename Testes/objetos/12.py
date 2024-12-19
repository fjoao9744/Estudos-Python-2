# dataclasses

from dataclasses import dataclass

@dataclass(frozen=True) # agora essa classe é imutavel
class Pessoa:
    nome : str
    idade: int
    sexo : str = "I"
    
    def apresentar(self):
        print(f"ola, meu nome é {self.nome}")
    
    
jorge = Pessoa("jorge", 12, "M")

jorge.apresentar()

# jorge.nome = "maria" # vai dar erro pq a classe é imutavel
