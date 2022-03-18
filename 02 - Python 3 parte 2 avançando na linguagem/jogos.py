import forca
import adivinhacao08

print('==' * 14)
print(f'{"ESCOLHA UM JOGO":-^28}')
print('==' * 14)


print("[1] - FORCA [2] - ADIVINHAÇÃO\n")

jogo = int(input("Qual jogo? "))
if (jogo == 1):
    print("Jogando forca")
    forca.jogar()
elif (jogo == 2):
    print("Jogando adivinhação")
    adivinhacao08.jogar()

