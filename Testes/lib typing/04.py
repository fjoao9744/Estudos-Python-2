from typing import Type

class Monster:
    def __init__(self, nome):
        self.nome = nome

def monster_instance(classe: type[Monster], name: str) -> Monster:
    return classe(name)

class Slime(Monster):
    pass

monster = monster_instance(Slime, "smogon")

print(monster.nome)
