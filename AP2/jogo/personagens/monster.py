import random
#from player import Player

class Monster:
    def __init__(self, name, reward):
        self.name = name
        self.level = random.randint(1,5)
        self.life = 100 + self.level*10
        self.defese = random.randint(1,50)
        self.force = random.randint(1,50)
        self.reward = reward
        
    def statusMonster(self):
        print("-" * 20)
        print(f"Nome: {self.name}\nVida: {self.life}\nNivel: {self.level}\nForça: {self.force}\nDefesa: {self.defese}")
        print("-" * 20)

    def takeDamage(self, amount):
        self.life -= amount
        if self.life < 0:
            self.life = 0

    def attack(self, player):# Player):
        damage = self.force - player.defese
        if damage > 0:
            player.takeDamage(damage)
        return damage

    def alive(self):
        return self.life > 0

if __name__ == "__main__":
    monster = Monster("Troll", 2)
    monster.statusMonster()
    print(monster.alive())
    monster.takeDamage(150)
    monster.statusMonster()
    print(monster.alive())

"""  

if __name__ == "__main__":
    m1 = Monster("a")
    print(Monster.esta_vivo(m1))
    m1.defender(15)
    print(m1.forca)
    print(m1.defesa)
    m2 = Monster("b")
    print(m2.forca)
    print(m2.defesa)
    m3 = Monster("c")
    print(m3.forca)
    print(m3.defesa)
    m4 = Monster("c")
    print(m4.forca)
    print(m4.defesa)

"""