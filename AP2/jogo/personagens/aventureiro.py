import random

class Aventureiro:
    mochila = [] # é pra ser do tipo item
    posicao = [0,0]
    forca = random.randint(10,18)
    defesa = random.randint(10,18)
    vida_max = random.randint(100, 120)
    vida_atual = vida_max

    #método construtor
    def __init__(self, nome):
        self.nome = nome

    def ver_atributos(self):
        print(self.forca)
        print(self.defesa)
        print(self.vida_atual)


    def ver_mochila(self):
        print(self.mochila)

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
        self.vida_atual -= x
        
    def esta_vivo(self):
        vivo = self.vida_atual > 0
        return vivo
    
    def coletar_item(self, item):
        self.mochila.append(item)

    def ver_mochila(self):
        print(self.mochila)

    def recuperar_vida(self, quantidade):
        self.vida = min(self.vida + (20 * quantidade), self.vida_max)

    def aumentar_forca(self, quantidade):
        self.forca += quantidade

    def aumentar_defesa(self, quantidade):
        self.defesa += quantidade


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
    Aventureiro.coletar_item(p1,5)
    Aventureiro.coletar_item(p1,'oi')
    Aventureiro.coletar_item(p1,'folk')
    Aventureiro.ver_mochila(p1)


    #atributos iniciais
    """
    Nome: informado pelo jogador assim que o jogo começa;
    Força: um inteiro aleatório entre 10 e 18;
    Defesa: um inteiro aleatório entre 10 e 18;
    Vida Máxima: um inteiro aleatório entre 100 e 120;
    Vida Atual: um inteiro, inicialmente igual à Vida Máxima;
    Mochila: uma lista de objetos do tipo Item, que se inicia vazia;
    Posição: uma lista com dois elementos, inicializado como [0, 0];
  
      #demais metodos


    def coletar(self):
        pass

    def usar_item(self):
        pass

    def ver_mochila(self):
        pass


    
          """
    