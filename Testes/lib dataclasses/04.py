from dataclasses import dataclass, field

@dataclass
class Pessoa:
    nome: str = field(repr=False) # esse atributo não aparecerá quando for printar
    idade: int = field(compare=False) # não tera os dunders __eq__ e nem __gt__

joao = Pessoa("joao", 18)
print(joao)


