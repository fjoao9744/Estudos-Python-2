class Pessoa:
    especie = "Humano"
    
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
        
        
print(Pessoa.__dict__)