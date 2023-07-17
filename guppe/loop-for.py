
"""
nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)

# exemplo de for 1

for letras in nome:
    print(letras)

for numb in lista:
    print(numb > 4)

for numero in range(0, 10):
    print(numero)

for indice, letra in enumerate(nome):
    print(nome[indice], end='')

"""



print('☆'.center(20)) #center(int) para centralizar a estrela
# construindo a árvore
for i in range(1, 20, 2):
    print(('*'*i).center(20))
# tronco da árvore
for r in range(2):
    print(('||').center(19))
# base da árvore
print('\====/'.center(19))
print()
