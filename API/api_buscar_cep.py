import requests


def buscar_cep(cep):

    lista = []
    dados = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    lista = dados.json()

    return lista

""" print(lista['cep'])
print(lista['logradouro'])
print(lista['complemento'])
print(lista['bairro'])
print(lista['localidade'])
print(lista['uf']) """
