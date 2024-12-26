# Classmethod

class Pessoa:
    especie = "Humano"
    
    def __init__(self, nome) -> None:
        self.nome = nome
        
    def apresentar(self):
        print(f"Ola meu nome é {self.nome}")
        
    @classmethod # esse decorador faz com que trabalhemos diretamente com a classe e não com uma instancia dela
    def mudar_especie(cls, new_especie):
        Pessoa.especie = new_especie
        
jorge = Pessoa("jorge")
maria = Pessoa("maria")

jorge.apresentar()

print(jorge.especie)
print(maria.especie)

jorge.mudar_especie("alien")

print(jorge.especie)
print(maria.especie) # muda a especie de maria pois esta mudadno uma varaivel da classe e não de uma instancia
