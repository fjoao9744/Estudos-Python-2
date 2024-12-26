# Herança

class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome
        
    def falar(self):
        print(f"o {self.nome} esta falando")
        
class Cachorro(Animal):
    def falar(self):
        print("au au!")

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome)
        self.cor = cor
        
    def falar(self):
        # super().falar() # esta herdando a função falar da classe mãe
        print("Miau!")
        
class Peixe(Animal):
    def __init__(self, nome):
        super().__init__(nome)
        
    def nadar(self):
        print(f"O {self.nome} esta nadando!")
    

        
rex = Cachorro("rex")
bola = Gato("bola", "azul")
gold = Peixe("gold")

print(rex.nome) # ele herdou o nome da classe mãe
rex.falar()

print(bola.nome)
bola.falar()

print(gold.nome)
gold.nadar()
gold.falar()