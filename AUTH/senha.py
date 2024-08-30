import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass

user = input("Informe seu nome de usuário do git: ")
password = input("Informe seu token/senha de usuário do git: ")
print("-"*30)

print("1 - Para listar os seus seguidores\n2 - Para seguir um usuário\n3 - Para deixar de seguir")
op = int(input("Qual opção? "))

if op ==1:
    response = requests.get(f'https://api.github.com/users/{user}/followers',
                auth = HTTPBasicAuth('user', password))
    
    

    if response.status_code == 200:
        for seguidor in response.json():
            print(seguidor['login'])
    else: 
        print("Algo de errado aconteceu.")


#para seguir
elif op == 2:
    username = input("Digite o nome do usuário que você deseja seguir: ")
    response = requests.put(f'https://api.github.com/user/following/{username}',
                auth = HTTPBasicAuth(user, password))
    
    if response.status_code == 204:
        print(f"Agora você está seguindo: {username}")
    else:
        print("Algo de errado aconteceu.")
    
elif op == 3:
    username = input("Digite o nome do usuário que você QUER DEIXAR de seguir: ")
    response = requests.delete(f'https://api.github.com/user/following/{username}',
                auth = HTTPBasicAuth(user, password))
    
    if response.status_code == 204:
        print(f"Você deixou de seguir: {username}")
    else:
        print("Algo de errado aconteceu.")
    



