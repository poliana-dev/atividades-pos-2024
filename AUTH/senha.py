import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass




user = input("Informe seu nome de usuário do git: ")
password = input("Informe seu token/senha de usuário do git: ")
print("-"*30)

print("1 - Para listar os seus seguidores\n2 - Para seguir um usuário\n3 - Para deixar de seguir")




user = input("para conhecer os usuarios de um user: ")

response = requests.get(f'https://api.github.com/users/{user}/followers',
            auth = HTTPBasicAuth('user', password))

for seguidor in response.json():
    print(seguidor['login'])


user = input("para conhecer os usuarios de um user: ")

response = requests.get(f'https://api.github.com/users/{user}/followers',
            auth = HTTPBasicAuth('user', password))

for seguidor in response.json():
    print(seguidor['login'])

print(response.status_code)



