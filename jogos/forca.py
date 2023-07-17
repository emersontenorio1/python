def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


    palavra_secreta = "banana"

    enforcou = False
    acertou = False
    erros = 0

    print("A palavra secreta tem {} letras".format(len(palavra_secreta)))
    letras_acertadas = []
    indice = 0
    for quandidade in palavra_secreta:
        letras_acertadas.append("_")
        print(letras_acertadas[indice], end=" ")
        indice += 1

    print()


    #equanto nao enforcou e nao acertou
    while not enforcou and not acertou:
        chute = input("Qual a letra? ").lower().strip()
        while len(chute) > 1:
            print("valor de do chute invalido, digite novamente")
            chute = input("Qual a letra? ").lower().strip()
        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                        letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
        print(letras_acertadas)
        enforcou = erros == len(palavra_secreta)
        acertou = "_" not in letras_acertadas

        print()
    if acertou:
        print('Você ganhou')
    else:
        print('Você perdeu')
    print("Fim do jogo")



if(__name__ == "__main__"):
    jogar()

