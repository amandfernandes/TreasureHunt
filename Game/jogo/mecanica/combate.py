# from jogo.personagens import aventureiro, monstro
# import random

from jogo.personagens import aventureiro, monstro

"""O combate se dá nas seguintes ações:

Fase do p1: ataca, armazenando o dano;
Fase do m1: defende, atualizando a vida dele;
Fase do m1: ataca, armazenando o dano;
Fase do p1: defende, atualizando a vida dele.
O combate encerra assim que um dos dois, p1 
ou m1, chega a uma vida menor que zero.

Encerramento
O jogo acaba quando (a) o p1 morre, ou (b) 
o p1 chega no tesouro."""

def combater(p1, m1):

    while p1.vida_atual >= 0 and m1.vida >= 0:
        print(f'P1: {p1.vida_atual} M1: {m1.vida}')
        dano = p1.atacar()
        m1.defender(m1, dano)
        print(f'P1: {p1.vida_atual} M1: {m1.vida}')
        dano = m1.atacar(m1)
        p1.defender(dano)
        print(f'P1: {p1.vida_atual} M1: {m1.vida}')
        print("-"*20)
    

if __name__ == "__main__":
    p1 = aventureiro.p1("mid")
    m1 = monstro.m1()
    combater(p1,m1)
'''
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
'''