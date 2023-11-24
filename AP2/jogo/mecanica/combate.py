from jogo.personagens import aventureiro, monstro

def combater(p1, m1):
    
    print(f'Aventureiro: {p1.vida_atual} de vida')
    print(f'Monstro: {m1.vida} de vida')
    while p1.vida_atual >= 0 and m1.vida >= 0:
        dano = p1.atacar()
        print(f'Aventureiro ataca! {dano} de dano!')
        m1.defender(dano)
        print(f'Monstro defende! {m1.vida} de vida')
        dano = m1.atacar()
        print(f'Monstro ataca! {dano} de dano!')
        p1.defender(dano)
        print(f'Aventureiro defende! {p1.vida_atual} de vida')
    print("-"*20)
    print(f'Aventureiro: {p1.vida_atual} vida, Monstro: {m1.vida} vida')
    

if __name__ == "__main__":
    p1 = aventureiro.p1("mid")
    m1 = monstro.m1()
    combater(p1,m1)