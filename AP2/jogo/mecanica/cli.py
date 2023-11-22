import random

from jogo.ativos import item, mapa, tesouro
from jogo.mecanica import combate
from jogo.personagens import aventureiro, monstro

def interagir_item(p1):
    p1.ver_mochila()
    escolha = input(print("Escolha um item para usar (digite o nome) ou pressione Enter para voltar: "))
    #while escolha not in p1.mochila:
     #   print("Item não encontrado.")
    #else:
    #    pass
    for escolha in p1.mochila:
       if escolha == item.nome:
           item.usar_item(p1)
           print(f"{item.nome} usado!")
           return
    print("Item não encontrado na mochila.")
    
    """
    - lista os itens da mochila
    - pede para o jogador escolher o item
    - usa o item caso exista, ou diz que não achou aquele item na mochila
    """

def movimentar(p1, dir):
    p1.mover(dir)
    opcoes = ["Nada", "Monstro", "Item"]
    turno = "".join(random.choices(opcoes, weights=[0.4, 0.4, 0.2]))
    print(turno)
    if turno == "Nada":
        return True
    elif turno == "Item":

        itens = [item.item1, item.item2, item.item3, item.item4, item.item5]

        it = random.choices(itens, weights=[0.5, 0.3, 0.05, 0.1, 0.05])
        p1.coletar_item(it)
        print(f"Item coletado:{it.nome}")
        breakpoint()
        return True

    elif turno == "Monstro":
        m1 = monstro.Monstro
        combate.combater(p1, m1)
        m1.vida = random.randint(10,100)
        if p1.vida_atual < 0:
            return False
        else:
            return True

    """
    - movimenta o aventureiro
    - se ele andou, seleciona uma das opções: nada, item ou monstro
    - se sorteou monstro, inicializa um monstro e começa um combate
    - se sorteou item, inicializa um item
    - retorna False se o aventureiro morrer, e True nos outros casos
    """

def jogo():
    nome = input("Deseja buscar um tesouro? Primeiro, informe seu nome: ")
    p1 = aventureiro.Aventureiro(nome)
    print(f"Saudações, {nome}! Boa sorte!")
    tes = tesouro.Tesouro()
    mapa.desenhar(p1.posicao, tes.posicao)
    print (tes.posicao) #teste

    while True:
        op = input("Insira o seu comando: ").upper()
        if op == "Q":
            print("Já correndo?")
            break

        if op == "T":
            p1.ver_atributos()
        elif op == "I":
            interagir_item(p1)
        elif op in ["W", "A", "S", "D"]:
            if movimentar(p1, op):
                mapa.desenhar(p1.posicao, tes.posicao)
            else:
                print("Game Over...")
                break
        else:
            print(f"{p1.nome}, não conheço essa! Tente novamente!")

        if p1.posicao == tes.posicao:
            print(f"Parabéns, {p1.nome}! Você encontrou o tesouro!")
            break

if __name__ == "__main__":
    jogo()
