import requests


def consultar_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if 'erro' not in data:
            return data
    return None


# Exemplo de uso
cep = input("Digite o cep: ")  # CEP de teste
resultado = consultar_cep(cep)

if resultado:
    print(f'CEP: {resultado["cep"]}')
    print(f'Logradouro: {resultado["logradouro"]}')
    print(f'Bairro: {resultado["bairro"]}')
    print(f'Cidade: {resultado["localidade"]}')
    print(f'Estado: {resultado["uf"]}')
else:
    print('CEP não encontrado.')