import random

from jogo.ativos import item, mapa, tesouro
from jogo.mecanica import combate
from jogo.personagens import aventureiro, monstro

def interagir_item(p1):
    p1.ver_mochila()
    escolha = input(print("Escolha um item para usar (digite o nome) ou pressione Enter para voltar: "))
    for item in p1.mochila:
        if item.nome == escolha:
            p1.usar_item(item)
            print(f"{item.nome} usado!")  
    else:
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

        itens = ["Força 1", "Força 2", "Vida 1", "Vida 2", "Defesa"]
        item_selecionado = "".join(random.choices(itens, weights=[0.1, 0.05, 0.5, 0.3, 0.05]))
        if item_selecionado == "Força 1":
            item1 = item.Item("Poção de Força", "Força", 1)
            it = item1
        elif item_selecionado == "Força 2":
            item2 = item.Item("Poção de Super Força", "Força", 2)
            it = item2
        elif item_selecionado == "Vida 1":
            item3 = item.Item("Poção de Vida", "Vida", 1)
            it = item3
        elif item_selecionado == "Vida 2":
            item4 = item.Item("Poção de Vida Longa", "Vida", 2)
            it = item4
        elif item_selecionado == "Defesa":
            item5 = item.Item("Poção de Defesa", "Defesa", 1)
            it = item5

        p1.coletar_item(it)
        print(f"Item coletado:{it.nome}")
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
