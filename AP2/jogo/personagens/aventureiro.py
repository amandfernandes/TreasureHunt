import random

class Aventureiro:
    mochila = []
    posicao = [0,0]
    forca = random.randint(10,18)
    defesa = random.randint(10,18)
    vida_max = random.randint(100, 120)
    vida_atual = vida_max

    #método construtor
    def __init__(self, nome):
        self.nome = nome

    def ver_atributos(self):
        print("-" * 20)
        print(f"Força Atual: {self.forca}")
        print(f"Defesa: {self.defesa}")
        print(f"Vida Atual: {self.vida_atual}")
        print(f"Vida Máxima: {self.vida_max}")
        print("-" * 20)

    def ver_mochila(self):
        print("-" * 20)
        print("Itens na mochila: ")
        for item in self.mochila:
            print(item.nome)
        print("-" * 20)

    def mover(self, dir):
        posicao = self.posicao
        if dir.lower() == "w":
            if posicao[1] > 0:
                posicao[1] -= 1
        elif dir.lower() == "s":
            if posicao[1] < 10:
                posicao[1] += 1
        elif dir.lower() == "d":
            if posicao[0] < 10:
                posicao[0] += 1
        elif dir.lower() == "a":
            if posicao[0] > 0:
                posicao[0] -= 1

    def atacar(self):
        return self.forca + random.randint(1,6)

    def defender(self, dano):
        x = dano - self.defesa
        if x < 0:
            x = 0
        self.vida_atual -= x

    def esta_vivo(self):
        return self.vida_atual >= 0
    
    def coletar_item(self, item):
        self.mochila.append(item)

    def recuperar_vida(self, quantidade):
        self.vida_atual = min(self.vida_atual + 20 * quantidade, self.vida_max)

    def aumentar_forca(self, quantidade):
        self.forca += quantidade

    def aumentar_defesa(self, quantidade):
        self.defesa += quantidade

    def usar_item(self, it1):
        if it1.tipo == "Vida":
            self.recuperar_vida(it1.intensidade)
        elif it1.tipo == "Força":
            self.aumentar_forca(it1.intensidade)
        elif it1.tipo == "Defesa":
            self.aumentar_defesa(it1.intensidade)
        self.mochila.remove(it1)


if __name__ == "__main__":
    p1 = Aventureiro("tay")
    Aventureiro.mover(p1, "d")
    print(Aventureiro.posicao)
    Aventureiro.mover(p1, "a")
    print(Aventureiro.posicao)
    Aventureiro.mover(p1, "s")
    print(Aventureiro.posicao)
    Aventureiro.mover(p1, "w")
    print(Aventureiro.posicao)
    print("-"*20)
    p1.ver_atributos()
    print("-"*20)
    print(p1.atacar())
    p1.defender(5)
    p1.ver_atributos()
    print("-"*20)
    print(p1.esta_vivo())
    print("-"*20)
    print(f"vida:{p1.vida_atual}")
    print(f"vida max:{p1.vida_max}")
    print("-"*20)
    dano = p1.atacar()
    p1.defender(dano)
    print(f"vida:{p1.vida_atual}")
    dano = p1.atacar()
    p1.defender(dano)
    print(f"vida:{p1.vida_atual}")
    dano = p1.atacar()
    p1.defender(dano)
    print(f"vida:{p1.vida_atual}")
    dano = p1.atacar()
    p1.defender(dano)
    print(f"vida:{p1.vida_atual}")