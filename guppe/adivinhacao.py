import random
print("**************")
print("Bem vindo ao jogo de adivinhação!")
print("**************")

numero_secreto = random.randrange(1, 101)


continuar = 0



while continuar == 0:
    chute = int(input("Qual o numero secreto: "))

    if chute < 1 or chute > 100:
        print("Você deve digitar um numero entre 1 e 100")
        print("POR FAVOR DIGITE UM NUMERO VALIDO DE ACORDO COM AS REGRAS")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto
    if acertou:
                print("você acertou o numero")
                break
    else:
        if (maior):
            print("O seu chute foi maior do que o número secreto!")
        elif (menor):
            print("O seu chute foi menor do que o número secreto!")

    continuar = int(input("Para continuar tentando digite 0 , qualquer tecla para sair: "))


