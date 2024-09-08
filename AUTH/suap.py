import requests
from getpass import getpass
import json
import os #vai verificar se o arquivo auth/suap_api/token.json existe no sistema de arquivos.



api_url = "https://suap.ifrn.edu.br/api/"

def autenticar():
    matricula = input("Informe a matrícula: ")
    password = getpass("Informe a senha:")
    print("-"*30)

    data = {"username":matricula,"password":password}

    response = requests.post(api_url+"v2/autenticacao/token/", json=data)
    return response.json()["access"] # o suap manda um token 


def main(api_url, token, anoLetivo):
    headers = {
        "Authorization": f'Bearer {token}'
    }
    
    response = requests.get(f"{api_url}v2/minhas-informacoes/boletim/{anoLetivo}/1", headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print("Erro ao obter boletim.")


if (os.path.isfile("AUTH/token.json")):
    with open("AUTH/token.json") as file:
        token = json.load(file)['token']
        anoLetivo=input("Informe o ano letivo: ")
        response = main(api_url, token, anoLetivo)

        for disciplina in response:
            print(f"{disciplina['disciplina']} - Média final: {disciplina['media_disciplina']}")  
else:
    token = autenticar()
    if token:  # Se a autenticação foi bem-sucedida
        with open("AUTH/token.json", "w") as file:
            data = {"token": token}
            json.dump(data, file)