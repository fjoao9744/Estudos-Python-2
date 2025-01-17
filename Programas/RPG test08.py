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
        dano = randrange(self.dano_min, self.dano_max + 1)
        return dano
        
    @property
    def hp(self):
        return self.__hp
    
    def tomar_dano(self, dano: int):
        self.__hp -= dano
        if self.__hp <= 0:
            self.__hp = 0
            
    def atacar(self, monster):
        dano = self.gerar_dano()
        monster.tomar_dano(dano)
    
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

class Slime:
    def __init__(self, nome = "Slime", level = 1):
        self.nome = nome
        self.level = level
        
        self.hp_max = 6 * self.level
        self.hp = 6 * self.level
        self.dano_min = 2 * self.level
        self.dano_max = 3 * self.level
        
    def tomar_dano(self, dano: int):
        self.hp -= dano
        if self.hp <= 0:
            self.hp = 0
    
    def atacar(self, player):
        dano = self.gerar_dano()
        player.tomar_dano(dano)
        
    def gerar_dano(self):
        dano = randrange(self.dano_min, self.dano_max + 1)
        return dano
    
def batalha(player, monster):
    while 1:
        print(player.ficha())
        print(monster.hp)
        if player.hp > 0:
            player.atacar(monster)
        else:
            break
        
        if monster.hp > 0:
            monster.atacar(player)
        else:
            break

joao = Player("joao")
slime_vermelho = Slime()
    
batalha(joao, slime_vermelho)