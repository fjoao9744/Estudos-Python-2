from random import randrange

class Player:
    def __init__(self, nome: str):
        self.nome = nome
        self.level = 1
        
        self.hp_max = 20
        self.__hp = 20
        
        self.dano_min = 2
        self.dano_max = 6
        self.crit = 9
        
    def gerar_dano(self):
        dano = randrange(self.dano_min, self.dano_max)
        return dano
        
    @property
    def hp(self):
        return self.__hp
    
    def tomar_dano(self, dano: int):
        self.__hp -= dano
        if self.__hp <= 0:
            self.__hp = 0
    
    def curar(self, cura: int):
        self.__hp += cura
        if self.__hp >= self.hp_max:
            self.__hp = self.hp_max
            
joao = Player("joao")

print(joao.hp)

joao.tomar_dano(10)

print(joao.hp)

joao.tomar_dano(300)

print(joao.hp)

joao.curar(15)

print(joao.hp)

joao.curar(15)

print(joao.hp)


        
        