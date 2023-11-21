def desenhar(personagem, tesouro):
    for y in range(10):
        for x in range(10):
            if personagem == [x, y]:
                print("@", end=" ")
            elif tesouro == [x, y]:
                print("X", end=" ")
            else:
                print(".", end=" ")
        print()

if __name__ == "__main__":
    desenhar([0, 0], [2, 4])
    print("-" * 12)
    desenhar([2, 1], [5, 0])
