from dataclasses import dataclass

@dataclass
class Especie:
    tempo_vida: int
    sexo: str
    
@dataclass
class Cachorro(Especie):
    raça: str
    
@dataclass
class BorderCollie(Cachorro):
    raça: str = "Border Collie"
    tempo_vida: int = 13

@dataclass
class Bulldog(Cachorro):
    raça: str = "Bulldog"
    tempo_vida: int = 9
    
dog = Bulldog(sexo="M") # toda especie tem um sexo, isso é a herança
border = BorderCollie(sexo="F")
