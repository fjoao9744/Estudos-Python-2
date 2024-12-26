# property e setter

class Pessoa:
    especie = "Humano"
    
    def __init__(self, nome, idade) -> None:
        self.__nome = nome
        self.__idade = idade
        
    def apresentar(self):
        print(f"Ola meu nome é {self.__nome}")
        
    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, idade):
        self.__idade = idade

jorge = Pessoa("jorge", 12)
jorge.apresentar()
     
print(jorge.idade) # ta acessando a função(do property) e não a variavel da instancia

jorge.idade = 15 # ta acessando a idade.setter

print(jorge.idade)

