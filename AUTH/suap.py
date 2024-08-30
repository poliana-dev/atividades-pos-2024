import requests
from getpass import getpass
import json


api_url = "https://suap.ifrn.edu.br/api/"


def autenticar():

    matricula = input("Informe a matrícula: ")
    password = getpass()
    print("-"*30)


    data = {"username":matricula,"password":password}

    response = requests.post(api_url+"v2/autenticacao/token/", json=data)
    return response.json()["access"] # o suap manda um token


def main():
    with open('suap_keys.json', "w+") as file:
        try:
            data = json.load(file)
        except json.decoder.JSONDecodeError:
            data = {}
            data['token'] = autenticar(api_url)
            json.dump(data,file)

    if not data['token']:
       data['token'] =  autenticar(api_url)

    token = data['token']

    headers = {
        "Authorization": f'Bearer {token}'
    }

    anoLetivo = input("Informe seu ano letivo: ")
    periodoLetivo = input("Informe seu periodo letivo: ")
    print(headers)

    response = requests.get(f"{api_url}v2/minhas-informacoes/boletim/{anoLetivo}/{periodoLetivo}/", headers=headers)

    print(response.text)
    print(response)