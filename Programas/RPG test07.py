class Slime:
    def __init__(self, nome = "Slime", level = 1):
        self.nome = nome
        self.level = level
        
        self.hp = 6 * self.level
        self.atk = 2 * self.level
        