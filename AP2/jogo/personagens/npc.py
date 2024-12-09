import google.generativeai as genai
import random
import re

from aventureiro import Aventureiro
from ativos import mapa 

genai.configure(api_key="API_KEY")

class NPC:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.humor = "neutro"

    def interact (self, player: Aventureiro):
        print(f"{player.nome}, essa função é somente implementada nas subclasses")
    

class Sage(NPC):
    def __init__(self, name):
        super().__init__(name)
    
    def interact(self, player):
        self.humor = random.choice("laconico", "desafiador", "benevolente")
        self.level = random.randint(1,5)

        model = genai.GenerativeModel("gemini-1.5-flash-latest")

        print("No meio do caminho, você encontra um velho sábio sentado sob uma árvore antiga. Seus olhos brilham com conhecimento, e ele parece saber mais sobre o tesouro do que você imagina.")
        print(f"Nivel: {self.level}")


        if self.humor == "laconico":
            laconicoPrompt = f"Faça um dialogo inciado com uma breve narrativa de jogo para caça tesouro, onde o {player.nome}, primeira pessoa, está em {mapa.context} e  encontra um sabio {self.humor} que não quer ajudar o jogador de maneira alguma. "
            dialogue = model.generate_content(laconicoPrompt).text
            print(dialogue)

        elif self.humor == "benevolente":
            benevolentePrompt = f"Faça um dialogo inciando com uma breve narrativa de jogo para caça tesouro, onde o {player.nome}, primeira pessoa, está em {mapa.context} e encontra um sabio {self.humor} o dialogo acaba antes dele dar uma dica deixando espaço para a dica"
            dialogue = model.generate_content(benevolentePrompt).text
            print(dialogue)
            self.getHint(player)

        elif self.humor == "desafiador" or self.humor == "neutro":
            desafiadorPrompt = f"Faça um dialogo inciando com uma breve narrativa de jogo para caça tesouro, onde o {player.nome}, primeira pessoa, está em {mapa.context} e  encontra um sabio {self.humor} o dialogo deve parar antes do sabio dizer a charado ao jogador deixa espaço para faze-la"
            dialogue = model.generate_content(desafiadorPrompt).text
            print(dialogue)
            self.advise(player)
        else:
            print("O sábio está indisponivel no momento.")

    def advise(self, player: Aventureiro):
        
        model = genai.GenerativeModel("gemini-1.5-flash-latest")

        riddlePrompt = f"{self.name} é um sábio de nível {self.level}. O jogador {player.nome} está em uma jornada e precisa de uma charada. Gere uma charada para  o jogador resolver. E ofereça 4 opções de respostas de 1 a 4. Não diga a resposta."
        try:
            riddle = model.generate_content(riddlePrompt).text
            riddleResponse = model.generate_content(f"Qual a resposta dessa charada {riddle}, responda apenas o valor (int), de 1 a 4.").text

            number = r'\d+'
            match = re.search(number, riddleResponse)
            if match:
                correctAnswer = int(match)
            else: 
                print("Resposta fornecida numérica inválida.")
                return None
            
            print(f"{self.name}: {riddle}")
            print("Escolha entre as alternativas:")
            self.askRiddle(player, correctAnswer)
        except Exception as e:
            print(f"Erro em gerar charada: {e}")

    def askRiddle(self, player: Aventureiro, correctAnswer):
        chances = 2
        while chances > 0:
            try:
                answer = int(input(f"{player.nome}: "))
                if 1 <= answer <= 4:
                    if answer == correctAnswer:
                        print(f"{self.name}: 'Você desvenda o enigma com uma clareza surpreendente. {self.getHint(player)}'")
                        break
                    else:
                        chances -= 1
                        if chances > 0:
                            print("O sábio observa em silêncio.")
                            print(f"{self.name}: 'Ainda não, tente novamente, o tempo é precioso.'")
                        else:
                            print("Você tentou, mas o destino não favoreceu sua resposta. O enigma permanece em silêncio, e a chance se esvai.")
                            break
            except ValueError:
                print("Escolha inválida, tente novamente.")
    
    def getHint(self, player: Aventureiro):
        model = genai.GenerativeModel("gemini-1.5-flash-latest")
        hintPrompt = f"Você está oferecendo uma dica para o jogador {player.nome}. Ele está em uma missão {mapa.context} para encontrar um tesouro ou itm essencial para completar sua missão."
        try:
            hint = model.generate_content(hintPrompt).text
            print(hint)
        except Exception as e:
            print(f"Erro ao gerar dica: {e}")
"""
class Healer(NPC):
    def __init__(self, name):
        super().__init__(name)
        self.power = 10*self.level

    def interact(self, player):
    
"""
        
        
