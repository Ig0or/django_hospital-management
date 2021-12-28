import requests

def consulta_cep(cep):
    for char in cep:
        if char == '-' or char == '.':
            cep = cep.replace(char, '')
    retorno_api = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    retorno_api_json = retorno_api.json()
    if retorno_api.status_code == 200 and 'erro' not in retorno_api_json:
        return retorno_api_json
