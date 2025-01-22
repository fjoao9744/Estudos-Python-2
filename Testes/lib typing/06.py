from typing import TypedDict

class Pessoa(TypedDict):
    nome: str
    idade: int
    
def apresentar(pessoa: Pessoa):
    print(f"meu nome é {pessoa["nome"]} e eu tenho {pessoa["idade"]} anos") 
    
apresentar({"nome":"joao", "idade": 19})
