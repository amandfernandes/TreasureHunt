"""
PROGRAMAÇÃO ESTRUTURADA - AP2
23-11-2023
PAULA LUIZA OLIVEIRA
AMANDA FERNANDES
"""
from jogo.personagens.player import Archer, Warrior, Mage, Monster

def loadInto(intoFile):
    try: 
        with open(intoFile, "r") as file:
            return file.read()
    except FileNotFoundError:
        return "Introdução não encontrada."

def characterChoice (name):
    print("Escolha a classe do seu personagem:\n1. Feiticeiro\n2. Guerreiro\n3. Arqueiro")
    choice = input("Escolha uma opção: ")
    if choice == "1":
        return Mage(name=name)
    elif choice == "2":
        return Warrior(name=name)
    elif choice == "3":
        return Archer(name=name)
    else:
        print("Opção inválida! Tente novamente.")
        return characterChoice()

def main():
    print(loadInto("AP2/introduction.txt"))

    print("Bem-vindo ao Treasure Hunt!")
    print("1. Iniciar Jogo\n2. Carregar Progresso\n3. Sair")
    choice = input("Escolha uma opção: ")
    if choice == "1":
        name = input("Deseja buscar um tesouro? Primeiro, informe seu nome: ")
        characterChoice(name)
        print(f"Saudações, {name}! Boa sorte!")
    elif choice == "2":
        print("Carregando progresso...")
    elif choice == "3":
        print("Até a próxima!")
        exit()
    else:
        print("Opção inválida!")
        main()

if __name__ == "__main__":
    main()

"""
from jogo.mecanica import cli

def main():
    cli.jogo()

if __name__ == "__main__":
    main()

"""