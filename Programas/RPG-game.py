from random import randint
npcs =[]

player = {
    "nome": "joao",
    "level":1,
    "exp": 0,
    "exp_max": 100,
    "hp": 100,
    "hp_max":100
}

def criar_monstro():
    level = randint(0, 50)
    new_npc = {
        "name": f"monstro #{level}",
        "level": level,
        "dano" : 5 * level,
        "hp": 100 * level
    }
    return new_npc

def gerar_npcs(num_npcs):
    for x in range(num_npcs):
        npcs.append(criar_monstro())
    
gerar_npcs(5)

print(npcs)