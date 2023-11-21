import random

class Monstro:
    forca = random.randint(5,25)
    defesa = random.randint(5,10)
    vida = random.randint(10,100)

    def __init__(self):
        pass

    def atacar(self):
        return self.forca
    
    def defender(self, dano):
        x = dano - self.defesa
        self.vida -= x

    def esta_vivo(self):
        vivo = self.vida > 0
        return vivo

if __name__ == "__main__":
    m1 = Monstro
    print(Monstro.esta_vivo(m1))
    
    """Atributos:
Força: um inteiro aleatório entre 5 e 25
Defesa: um inteiro aleatório entre 5 e 10
Vida: um inteiro aleatório entre 10 e 100
Métodos:
Atacar: retorna um inteiro igual à força;
Defender: recebe como parâmetro um valor de dano, 
e reduz desse valor a defesa do monstro. 
O valor final é reduzido da vida atual do monstro;

Esta vivo: retorna um booleano informando se o mosntro está vivo."""