
n = int(input())

lista = []

for valores in range(n+1):
    lista.append(valores)

for inteiros in lista:
    if inteiros > 0:
        print(inteiros, end="")
