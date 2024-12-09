import random

class Treasure:
    def __init__(self, mapInstance):
        self.map = mapInstance.map
        self.width = mapInstance.width
        self.height = mapInstance.height
        self.treasurePosition = None

    def placeTreasure(self):
        while True:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)

            if self.map[y][x] == ".":
                self.treasurePosition = [x, y]
                self.map[y][x] = "X" 
                break

    def getTeasurePosition(self):
        return self.treasurePosition

if __name__ == "__main__":
    from mapa import MysteriousFlorest, UndergroundCave
    florest = MysteriousFlorest(10,10)
    treasure = Treasure(florest)
    treasure.placeTreasure()
    florest.display()
    print(f"Tesouro posicionado em: {treasure.getTeasurePosition()}")
    print("-" * 20)
    cave = UndergroundCave(20,10)
    treasure = Treasure(cave)
    treasure.placeTreasure()
    cave.display()
    print(f"Tesouro posicionado em: {treasure.getTeasurePosition()}")

"""
class Tesouro:
    
     while True:
        posicao = [random.randint(0, 9), random.randint(0, 9)]
        if posicao != [0, 0]:
            break


if __name__ == "__main__":
    print(Tesouro.posicao)
"""
