from dataclasses import dataclass
from InquirerPy.resolver import prompt

class Entity:
    def __init__(self, nome, hp, atk):
        self.nome = nome
        self.hp = hp
        self.atk = atk
        self.moves = []

class Player(Entity):
    def __init__(self, nome, hp, atk):
        super().__init__(nome, hp, atk)
        self.__exp = 0
        self.moves = [Move("soco", 1, None)]
        
    def exp_owner(self, exp):
        self.__exp += exp
        
    @property
    def exp(self):
        return self.__exp
        
    def atacar(self, monster, move):
        atk = self.atk + move.atk
        monster.hp -= atk
        
    def show_moves(self):
        return [move for move in self.moves]
        
    def add_move(self, move):
        self.moves.append(move)

class Effect:
    pass

@dataclass
class Move:
    nome: str
    atk: int
    effect: Effect | None

class Main:
    @staticmethod
    def batalha(player, monster):
        while 1:
            print(f"{player.nome}: {player.hp}")
            print(f"{monster.nome}: {monster.hp}")
            atk = prompt({"type":"list","message":"Qual movimento você escolhe:", "choices": player.show_moves()})
            player.atacar(monster, atk[0])
            print(f"{player.nome} atacou {monster.nome}")
            if monster.hp <= 0:
                print(f"{player.nome} venceu a batalha!")
                print(f"{player.nome} ganhou {monster.exp} de exp!")
                player.exp_owner(monster.exp)
                break
            
            monster.atacar(player)
            print(f"{monster.nome} atacou {player.nome}")
            if player.hp <= 0:
                print(f"{monster.nome} venceu a batalha!")
                break


class Monster(Entity):
    def __init__(self, nome, hp, atk, exp=1):
        super().__init__(nome, hp, atk)
        self.exp = exp
        
    def atacar(self, player):
        player.hp -= self.atk


joao = Player("joao", 20, 6)
joao.add_move(Move("soco", 1, None))
joao.add_move(Move("soco", 1, None))
joao.add_move(Move("soco", 1, None))

slime = Monster("slime", 15, 4, 30)
print(joao.moves[1])
print(joao.exp)
Main.batalha(joao, slime)
print(joao.exp)

            
            

    
    