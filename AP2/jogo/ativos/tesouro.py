import random

class Tesouro:
    
 
     while True:
        posicao = [random.randint(0, 9), random.randint(0, 9)]
        if posicao != [0, 0]:
            break

    #def __init__(self):
     #   self.posicao = [random.randint(1,9), random.randint(1,9)]

if __name__ == "__main__":
    print(Tesouro.posicao)