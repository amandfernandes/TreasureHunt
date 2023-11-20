from jogo.personagens import aventureiro, monstro
import random

def atacar():
    return random.randint(1,10)

def defender (self, dano):
    self.atual -= dano

while aventureiro.atual > 0 and monstro.vida > 0:
    monstro.dano = aventureiro.atacar()
    monstro.defender(monstro.dano)

    if monstro.vida <= 0:
        print("Monstro derrotado!")
        break

    aventureiro.dano = monstro.atacar()
    aventureiro.defender(aventureiro.dano)

    if aventureiro.atual <= 0:
        print("Você foi derrotado!")
        break
