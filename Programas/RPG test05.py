from random import randrange
import pandas as pd

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
            
    def level_up(self):
        if self.level < 20:
            self.level += 1
            self.hp_max += self.hp_max // 4
            self.dano_min += self.dano_min // 2
            self.dano_max += self.dano_max // 3
            self.crit = self.dano_max + self.dano_min
            self.curar(self.hp_max // 4)
            
    def ficha(self):
        status = {
            "atributos" : ["nome","level","max_hp","hp","dano_min","dano_max","crit"],
            "valores": [self.nome,self.level,self.hp_max,self.__hp,self.dano_min,self.dano_max,self.crit]
        }
        
        df = pd.DataFrame(status)
        
        print(df.to_string(index=False))

joao = Player("joao")

for c in range(20):
    joao.ficha()
    joao.level_up()