import requests

def retorna_endereco(cep):
    url = 'https://viacep.com.br/ws/{}/json'.format(cep)
    r = requests.get(url)
    dados = r.json()
    bairro = dados.get('bairro')
    cidade = dados.get('localidade')
    uf = dados.get('uf')
    return bairro, cidade, uf


bairro, cidade, uf = retorna_endereco('88134597')

print(cidade, bairro, uf)