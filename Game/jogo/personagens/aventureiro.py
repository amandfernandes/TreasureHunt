import random

class Personagem:
    forca = random.randint(10,18)
    defesa = random.randint(10,18)
    max = random.randint(100,120)

    dano = 0

    mochila = []

    posição = [0,0]

    def vid (self,forca,defesa,max,dano):
        self.max = max
        self.atual = max
        self.forca = forca
        self.defesa = defesa
        self.dano = dano
    
    def life (self, intensidade):
        nova = min(self.max, self.atual + 20* intensidade)
        self.atual = nova

    def streght (self, intensidade):
        self.forca = self.forca + intensidade

    def defense (self, intensidade):
        self.defesa = self.defesa + intensidade


    
    

"""
posicao = [0, 0]

def move(dir):
    if dir.lower() == "w":
        if posicao[1] > 0:
            posicao[1] -= 1
    elif dir.lower() == "s":
        if posicao[1] < 5:
            posicao[1] += 1
    elif dir.lower() == "d":
        if posicao[0] < 5:
            posicao[0] += 1
    elif dir.lower() == "a":
        if posicao[0] > 0:
            posicao[0] -= 1

if __name__ == "__main__":
    print(posicao)
    move("d")
    print(posicao)
    move("a")
    print(posicao)
    move("s")
    print(posicao)
    move("w")
    print(posicao)
"""