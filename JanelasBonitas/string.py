"""Uma marca multinacional recém-inaugurada decidiu basear o logotipo de sua empresa nos três caracteres mais comuns do nome da empresa. Eles agora estão experimentando várias combinações de nomes e logotipos de empresas com base nessa condição. Dada uma string, que é o nome da empresa em letras minúsculas, sua tarefa é localizar os três caracteres mais comuns na sequência.

Imprima os três caracteres mais comuns junto com sua contagem de ocorrências.
Classifique em ordem decrescente de contagem de ocorrências.
Se a contagem de ocorrências for a mesma, classifique os caracteres em ordem alfabética.
Por exemplo, de acordo com as condições descritas acima,

GOOGLE teria o logo com as letras G,O,E.

Formato de entrada

Uma única linha de entrada contendo a string S.
Imprima os três caracteres mais comuns junto com sua contagem de ocorrências, cada um em uma linha separada.
Classifique a saída em ordem decrescente de contagem de ocorrências.
Se a contagem de ocorrências for a mesma, classifique os caracteres em ordem alfabética.


"""

s = input("Digite o nome da empresa: ")
def top_three_common_characters(s):
    char_count = {}  # Dicionário para armazenar a contagem de caracteres
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1  # Incrementa a contagem para o caractere atual

    sorted_chars = sorted(char_count.items(), key=lambda x: (-x[1], x[0]))  # Classifica com base na contagem e na ordem alfabética
    return sorted_chars[:3]  # Retorna os três caracteres mais comuns

# Exemplo de uso

result = top_three_common_characters(s)

# Imprime o resultado
for char, count in result:
    print(char, count)