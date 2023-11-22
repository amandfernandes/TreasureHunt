from personagens import aventureiro
import random
class Item:

    def __init__(self, nome, tipo, intensidade):
        self.nome = nome
        self.tipo = tipo
        self.intensidade = intensidade

    def usar_item(self):
        if self.tipo == "Vida":
            aventureiro.recuperar_vida(self.intensidade)
        elif self.tipo == "Forca":
            aventureiro.aumentar_forca(self.intensidade)
        elif self.tipo == "Defesa":
            aventureiro.aumentar_defesa(self.intensidade)

    def gerar_posicao_item():
        return [random.randint(0, 5), random.randint(0, 5)]
        
# Inicialização dos itens
    item1 = gerar_posicao_item()
    item2 = gerar_posicao_item()
    item3 = gerar_posicao_item()

# Verifica se os itens estão na mesma posição e refaz o sorteio se necessário
    while item1 == item2 or item1 == item3 or item2 == item3:
        item2 = gerar_posicao_item()
        item3 = gerar_posicao_item()
        
item1 = Item("Porção de Vida", "Vida", 20)
item2 = Item("Porção de Defesa", "Defesa", 1)
item3 = Item("Porção de Força", "Força", 1)


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