import random

class Map():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map =  self.createMap()

    def createMap(self):
        raise NotImplementedError("Método implementado nas subclasses.")
    
    def display(self):
        for line in self.map:
            print("  ".join(line))


class MysteriousFlorest(Map):
    def createMap(self):
        map = []
        for _ in range(self.height):
            line = []
            for _ in range(self.width):
                if random.random() < 0.2:
                    line.append("🌲")
                else:
                    line.append(".")
            map.append(line)
        return map
    
class UndergroundCave(Map):
    def createMap(self):
        map = []
        for _ in range(self.height):
            line = []
            for _ in range(self.width):
                if random.random() < 0.3:

                    line.append("▒")
                else:
                    line.append(".")
            map.append(line)
        return map
           

if __name__ == "__main__":
    florest = MysteriousFlorest(10,10)
    florest.display()
    print("-" * 20)
    cave = UndergroundCave(20,10)
    cave.display()
    print("-" * 20)

        



"""
def desenhar(personagem, tesouro):
    for y in range(10):
        for x in range(10):
            if personagem == [x, y]:
                print("@", end=" ")
            elif tesouro == [x, y]:
                print("X", end=" ")
            else:
                print(".", end=" ")
        print()
    
def context():
    print("Floresta")

if __name__ == "__main__":
    desenhar([0, 0], [2, 4])
    print("-" * 12)
    desenhar([2, 1], [5, 0])
"""
