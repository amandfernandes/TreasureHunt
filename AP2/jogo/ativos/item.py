from jogo.personagens import aventureiro
import random

class Item:

    def __init__(self, nome, tipo, intensidade):
        self.nome = nome
        self.tipo = tipo
        self.intensidade = intensidade


if __name__ == "__main__":
    ex1 = Item("Poçao 1", "Força", 2)
    ex2 = Item("Poçao 2", "Vida", 2)
    ex3 = Item("Poçao 3", "Defesa", 1)
    print(ex1.nome, ex1.tipo, ex1.intensidade)
    print(ex2.nome, ex2.tipo, ex2.intensidade)
    print(ex3.nome, ex3.tipo, ex3.intensidade)