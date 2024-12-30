class Entity:
    def __init__(self, nome, hp, atk):
        self.nome = nome
        self.hp = hp
        self.atk = atk

class Player(Entity):
    def __init__(self, nome, hp, atk):
        super().__init__(nome, hp, atk)
        self.__exp = 0
        
    def exp_owner(self, exp):
        self.__exp += exp
        
    def atacar(self, monster):
        monster.hp -= self.atk

class Monster(Entity):
    def __init__(self, nome, hp, atk, exp=1):
        super().__init__(nome, hp, atk)
        self.exp = exp
        
    def atacar(self, player):
        player.hp -= self.atk


p1 = Player("joao", 20, 5)
slime = Monster("slime", 15, 4, 30)

def batalha(player, monster):
    while True:
        player.atacar(monster)
        if monster.hp <= 0:
            print("o monstro morreu")
            break
   
        monster.atacar(player)
        if player.hp <= 0:
            print("o player morreu")
            break
        
batalha(p1, slime)

