# __module__

class Pessoa:
    especie = "Humano"
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
        
jorge = Pessoa("jorge", 18)

print(jorge.__module__) # retorna __main__ pq ele foi criado no __main__(ele funciona como um __name__)

def criar_pessoa():
    maria = Pessoa("maria", 18)
    
    print(maria.__module__) # faz a mesma coisa, ele foi criado no script principal
    
criar_pessoa() 

