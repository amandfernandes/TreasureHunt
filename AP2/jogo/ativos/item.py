from jogo.personagens import aventureiro
import random

class Item:

    def __init__(self, nome, tipo, intensidade):
        self.nome = nome
        self.tipo = tipo
        self.intensidade = intensidade

    def usar_item(self, p1):
        if self.tipo == "Vida".lower:
            aventureiro.recuperar_vida(p1, self.intensidade)
        elif self.tipo == "Forca".lower:
            aventureiro.aumentar_forca(p1, self.intensidade)
        elif self.tipo == "Defesa".lower:
            aventureiro.aumentar_defesa(p1, self.intensidade)

item1 = Item("Poção de Vida", "Vida", 1)
item2 = Item("Poção de Vida", "Vida", 2)
item3 = Item("Poção de Defesa", "Defesa", 1)
item4 = Item("Poção de Força", "Força", 1)
item5 = Item("Poção de Força", "Força", 2)

if __name__ == "__main__":
    print(item1.nome, item1.tipo, item1.intensidade)
    print(item2.nome, item2.tipo, item2.intensidade)
    print(item3.nome, item3.tipo, item3.intensidade)


""""    
Atributos:
Nome: nome do item;
Tipo: classificação do item;
Intensidade: bônus sobre o atributo (a depender do tipo);
"""
""""    
Atributos:
Nome: nome do item;
Tipo: classificação do item;
Intensidade: bônus sobre o atributo (a depender do tipo);
"""