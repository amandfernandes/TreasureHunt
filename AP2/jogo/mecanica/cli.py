import random
from datetime import time

from AP2.jogo.personagens import player
from jogo.ativos import item, mapa, tesouro
from jogo.mecanica import combate
from AP2.jogo.personagens import monster

def interagir_item(p1):
    if len(p1.mochila) == 0:
        print("Mochila Vazia")
    else:
        p1.ver_mochila()
        escolha = input(print("Escolha um item para usar (digite o nome): "))
        for item in p1.mochila:
            if item.nome == escolha:
                p1.usar_item(item)
                print(f"{item.nome} usado!")  
            else:
                print("Item não encontrado na mochila.")


def movimentar(p1, dir, monstros):
    p1.mover(dir)
    opcoes = ["Nada", "Monstro", "Item"]
    turno = "".join(random.choices(opcoes, weights=[0.4, 0.4, 0.2]))
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
        print(f"Item coletado: {it.nome}")
        return True

    elif turno == "Monstro":
        i = len(monstros) - 1
        nome = str(i)
        monstros[i] = monster.Monstro(nome)
        combate.combater(p1, monstros[i])
        monstros.append("")
        if p1.esta_vivo():
            return True
        else:
            return False

def dificuldade():
    print("(1) Fácil\n(2) Normal\n(3) Difícil")
    dif = input(print("Selecione uma dificuldade (escolha o número): "))
    if dif == "2":
        print("Você tem 20 turnos para encontrar o tesouro!")
        return 20
    elif dif == "3":
        print("Você tem 10 turnos para encontrar o tesouro!")
        return 10 
    else:
        print("Nível fácil selecionado por padrão.")
        return 999

def jogo():
    nome = input("Deseja buscar um tesouro? Primeiro, informe seu nome: ")
    p1 = player.Aventureiro(nome)
    dif = dificuldade()
    print(f"Saudações, {nome}! Boa sorte!")
    tes = tesouro.Tesouro()
    mapa.desenhar(p1.posicao, tes.posicao)
    monstros = [""]
    movimentos = 0


    while True:
        op = input(f"Insira o seu comando (Turno {movimentos}): ").upper()
        if op == "Q":
            print("Já correndo?")
            break

        if op == "T":
            p1.ver_atributos()
        elif op == "I":
            interagir_item(p1)
        elif op in ["W", "A", "S", "D"]:
            if movimentar(p1, op, monstros):
                mapa.desenhar(p1.posicao, tes.posicao)
                movimentos += 1
            else:
                print("Game Over...")
                break
        else:
            print(f"{p1.nome}, não conheço essa! Tente novamente!")

        if p1.posicao == tes.posicao:
            print(f"Parabéns, {p1.nome}! Você encontrou o tesouro!")
            break

        elif movimentos >= dif:
            print("Você perdeu... :(")
            break

if __name__ == "__main__":
    jogo()
