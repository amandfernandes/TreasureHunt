import random

from jogo.ativos import item, mapa, tesouro
from jogo.mecanica import combate
from jogo.personagens import aventureiro, monstro

def interagir_item(p1):
    """
    - lista os itens da mochila
    - pede para o jogador escolher o item
    - usa o item caso exista, ou diz que não achou aquele item na mochila
    """
    pass

def movimentar(p1, dir):
    
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
    mapa.desenhar(p1, tes)

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
                mapa.desenhar(p1, tes)
            else:
                print("Game Over...")
                break
        else:
            print(f"{p1.nome}, não conheço essa! Tente novamente!")

        if p1.posicao == tes.posicao:
            print(f"Parabéns, {p1.nome}! Você encontrou o tesouro!")
            break