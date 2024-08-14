import requests

api_url= 'https://jsonplaceholder.typicode.com/users/'

print("1 - para listar\n2- para listar tarefa \n3- para CRUD")
campo = int(input("Informe: "))

if campo == 1:
    response = requests.get(api_url).json()
    for user in response:
        print(f"{user['id']} - {user['name']}")

elif campo == 2:
    user_id= int(input("Digite o IDENTIFICADOR do usuário: "))
    response = requests.get(f"{api_url}/{user_id}/todos").json()

    for todo in response:
        print(f"{todo['title']}")

elif campo == 3:
    print("1 - para criar usuário\n2 - listar dados de um usuário\n3 - para atualizar dados do usuário\n4 - para deletar usuário")
    
    campo = int(input("Informe: "))
    
    if campo == 1:
        pass


# users faz um get da api trazendo o dado desejado diretamente sem ter todos de uma vez
# users = requests.get(f"https://jsonplaceholder.typicode.com/users/{campo}")
# user= users.json()

# print(f"{user['name']}")


