import os

class World:
    def __init__(self, player):
        self.map_generator = lambda: [[0 for x in range(10)] for y in range(10)]
        
        self.map = self.map_generator()
        self.player = player
        self.player_positionY = len(self.map) // 2
        self.player_positionX = len(self.map[0]) // 2

        self.map[self.player_positionY][self.player_positionX] = player
        
    def position_redefine(self):
        self.map[self.player_positionY][self.player_positionX] = self.player
        
    def walk_up(self):
        self.player_positionY -= 1
        self.position_redefine()
        self.map[self.player_positionY + 1][self.player_positionX] = 0
    
    def walk_dowm(self):
        self.player_positionY += 1
        self.position_redefine()
        self.map[self.player_positionY - 1][self.player_positionX] = 0
        
    def walk_right(self):
        self.player_positionX += 1
        self.position_redefine()
        self.map[self.player_positionY][self.player_positionX - 1] = 0
        
    def walk_left(self):
        self.player_positionX -= 1
        self.position_redefine()
        self.map[self.player_positionY][self.player_positionX + 1] = 0
        
w = World(1)

while 1:
    for map in w.map:
        print(map)
    
    moviment = input("andar:  ")
    match moviment:
        case "w":
            w.walk_up()
        case "s":
            w.walk_dowm()
        case "d":
            w.walk_right()
        case "a":
            w.walk_left()
            
    os.system("cls")
            
    
