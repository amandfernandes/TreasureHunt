import random

class Monstro:
    
    def __init__(self, nome):
        self.nome = nome
        forca = random.randint(5,25)
        defesa = random.randint(5,10)
        vida = random.randint(10,100)
        self.forca = forca
        self.defesa = defesa
        self.vida = vida

    def atacar(self):
        return self.forca
    
    def defender(self, dano):
        x = dano - self.defesa
        if x < 0:
            x = 0
        self.vida -= x

    def esta_vivo(self):
        vivo = self.vida >= 0
        return vivo
    

if __name__ == "__main__":
    m1 = Monstro("a")
    print(Monstro.esta_vivo(m1))
    m1.defender(15)
    print(m1.forca)
    print(m1.defesa)
    m2 = Monstro("b")
    print(m2.forca)
    print(m2.defesa)
    m3 = Monstro("c")
    print(m3.forca)
    print(m3.defesa)
    m4 = Monstro("c")
    print(m4.forca)
    print(m4.defesa)

