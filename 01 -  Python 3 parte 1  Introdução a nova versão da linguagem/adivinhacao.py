# adivinhacao.py
import random

def jogar():

    print('==' * 17)
    print('Bem vindo ao jogo de Adivinhação!')
    print('==' * 17)

    total_de_tentativas = 0
    pontos = 1000


    while True:

        print('Escolha um nível de dificuldade!\n')
        print('[1] - FÁCIL [2] - MÉDIO [3] - DIFÍCIL\n')
        
        escolha = ' ' 
        while escolha not in '123':
            escolha= str(input('Digite sua esolha: '))
        if escolha == '1':
            total_de_tentativas = 20
        elif escolha == '2':
            total_de_tentativas = 10
        elif escolha == '3':
            total_de_tentativas = 5
    
        numero_secreto = random.randrange(1, 101)

        for rodada in range(1, total_de_tentativas + 1):
            print(f'Tentativa {rodada} de {total_de_tentativas}')
            chute = int(input('Digite um número entre 1 e 100: '))
            print(f'Você digitou {chute}.')

            if chute < 1 or chute > 100:
                print('Você deve digitar um número entre 1 e 100')
                continue

            acertou = chute == numero_secreto
            maior = chute > numero_secreto
            menor = chute < numero_secreto

            if acertou:
                print(f'Parabéns, você acertou. O número secreto era {numero_secreto}. Você fez {pontos} pontos.')
                break
            else:
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos  

                if maior:
                    print('Errou! Seu chute foi maior que o número secreto!')
                    if (rodada == total_de_tentativas):
                        print(f'O número secreto era {numero_secreto}. Você fez {pontos}pontos.')

                elif menor:
                    print('Errou! Seu chute foi menor que o número secreto!')  
                    if (rodada == total_de_tentativas):
                        print(f'O número secreto era {numero_secreto}. Você fez {pontos} pontos.')

        print(f'O número que pensei foi {numero_secreto}')
            
        print('FIM DO JOGO!')

        resposta = ' '
        while resposta not in 'SN':
            try:
                resposta = str(input('JOGAR NOVAMENTE [s/n] ? ')).upper().strip()[0]
            except:
                print('Responda apenas "s" ou "n" ')
        if resposta == 'N':
            break

if(__name__ == "__main__"):
    jogar()
    