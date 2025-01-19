import random
from .monster import Monster

class Player:
    def __init__(self, name, character):
        self.name = name
        self.character = character
        self.maxLife = 100
        self.life = self.maxLife
        self.inventory = []
        self.level = 1
        self.experience = 0
        self.defese = 10
        self.force = 10

    def status(self):
        print("-" * 20)
        print(f"Nome: {self.name}\nClasse: {self.character}\nVida: {self.life}\nNivel: {self.level}\nXP: {self.experience}\nForça: {self.force}\nDefesa: {self.defese}")
        print("-" * 20)

    def addExperience(self, xp):
        self.experience += xp
        if self.experience >= self.level * 100:
            self.levelUp()
    
    def levelUp(self):
        self.level += 1
        self.life += 10
        self.force += 10
        self.defese += 10
        print("-" * 20)
        print(f"{self.name} subiu para o nivel {self.level}")
        print("-" * 20)

    def takeDamage(self, amount):
        self.life -= amount
        if self.life < 0:
            self.life = 0

    def attack(self, monster: Monster):
        damage = self.force - monster.defense
        if damage > 0:
            monster.takeDamage(damage)
        return damage
    
    def alive(self):
        return self.life > 0
    
class Archer(Player):
    def __init__(self, name):
        super().__init__(name, "Arqueiro")
        self.force = 12  
        self.defese = 8  
        self.rangeAttack = 15
    
    def quickAttack(self, monster: Monster):
        damage = self.rangeAttack - monster.defese
        if damage > 0:
            monster.takeDamage(damage)
        print(f"{self.name} atacou rapidamente com uma flecha!")
        return damage

    def rainArrows(self, monster: Monster):
        damage = self.rangeAttack // 2
        if damage > 0:
            monster.takeDamage(damage)
        print(f"{self.name} lançou uma chuva de flechas!")
        return damage

class Mage(Player):
    def __init__(self, name):
        super().__init__(name, "Feiticeiro")
        self.force = 8  
        self.defese = 6  
        self.mana = 100 
        self.magicDamage = 20

    def fireMagic(self, monster: Monster):
        if self.mana >= 10:
            self.mana -= 10
            damage = self.magicDamage - monster.defese
            if damage > 0:
                monster.takeDamage(damage)
            print(f"{self.name} lançou uma bola de fogo!")
            return damage
        else:
            print(f"{self.name} não tem mana suficiente para lançar magia de fogo!")
            return 0

    def magicShield(self):
        print(f"{self.name} usou um escudo mágico!")
        self.defese += 5

class Warrior(Player):
    def __init__(self, name):
        super().__init__(name, "Guerreiro")
        self.force = 20  
        self.defese = 20 
        self.healthRegeneration = 5
    
    def ironFist(self, monster: Monster):
        damage = self.force * 2 - monster.defese
        if damage > 0:
            monster.takeDamage(damage)
        print(f"{self.name} desferiu um golpe devastador, Punho de ferro!")
        return damage

    def ironWall(self):
        print(f"{self.name} usou sua defesa indestrutivel, Muralha de ferro!")
        self.defese += 10
        return self.defese


if __name__ == "__main__":
    p1 = Player("tay","Guerreiro")
    p1.status()
    p1.addExperience(120)
    p1.status()
    player1 = Archer("Archer")
    player1.status()
    player1.quickAttack(Monster("Goblin", 3))
    player2 = Mage("Mage")
    player2.status()
    player2.fireMagic(Monster("Orc", 4))
    player3 = Warrior("Warrior")
    player3.status()
    player3.ironFist(Monster("Troll", 5))

"""
    posicao = [0,0]


    def ver_mochila(self):
        print("-" * 20)
        print("Itens na mochila: ")
        for item in self.mochila:
            print(item.nome)
        print("-" * 20)

    def mover(self, dir):
        posicao = self.posicao
        if dir.lower() == "w":
            if posicao[1] > 0:
                posicao[1] -= 1
        elif dir.lower() == "s":
            if posicao[1] < 10:
                posicao[1] += 1
        elif dir.lower() == "d":
            if posicao[0] < 10:
                posicao[0] += 1
        elif dir.lower() == "a":
            if posicao[0] > 0:
                posicao[0] -= 1
    
    def coletar_item(self, item):
        self.mochila.append(item)

    def recuperar_vida(self, quantidade):
        self.vida_atual = min(self.vida_atual + 20 * quantidade, self.vida_max)

    def aumentar_forca(self, quantidade):
        self.forca += quantidade

    def aumentar_defesa(self, quantidade):
        self.defesa += quantidade

    def usar_item(self, it1):
        if it1.tipo == "Vida":
            self.recuperar_vida(it1.intensidade)
        elif it1.tipo == "Força":
            self.aumentar_forca(it1.intensidade)
        elif it1.tipo == "Defesa":
            self.aumentar_defesa(it1.intensidade)
        self.mochila.remove(it1)


if __name__ == "__main__":
    p1 = Aventureiro("tay")
    Aventureiro.mover(p1, "d")
    print(Aventureiro.posicao)
    Aventureiro.mover(p1, "a")
    print(Aventureiro.posicao)
    Aventureiro.mover(p1, "s")
    print(Aventureiro.posicao)
    Aventureiro.mover(p1, "w")
    print(Aventureiro.posicao)
    print("-"*20)
    p1.ver_atributos()
    print("-"*20)
    print(p1.atacar())
    p1.defender(5)
    p1.ver_atributos()
    print("-"*20)
    print(p1.esta_vivo())
    print("-"*20)
    print(f"vida:{p1.vida_atual}")
    print(f"vida max:{p1.vida_max}")
    print("-"*20)
    dano = p1.atacar()
    p1.defender(dano)
    print(f"vida:{p1.vida_atual}")
    dano = p1.atacar()
    p1.defender(dano)
    print(f"vida:{p1.vida_atual}")
    dano = p1.atacar()
    p1.defender(dano)
    print(f"vida:{p1.vida_atual}")
    dano = p1.atacar()
    p1.defender(dano)
    print(f"vida:{p1.vida_atual}")
"""