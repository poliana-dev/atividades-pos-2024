from xml.dom.minidom import parse

# determio o caminho do arquivo que desejo
caminho = parse("./XML_DTD/atividade01/cardapio.xml")

# 'crio" a raiz
cardapio = caminho.documentElement
pratos= cardapio.getElementsByTagName('prato') #pego o elemento apartir da raiz

print("\nSegue a lista dos nossos pratos:\n")

id_ref=0
for prato in pratos:
    id = prato.getAttribute('id')
    nome = prato.getElementsByTagName('nome')[0].firstChild.nodeValue
    # descricao = prato.getElementsByTagName('descricao')[0].firstChild.nodeValue
    # ingredientes = prato.getElementsByTagName('ingredientes')[0].firstChild.nodeValue 
    # preco = prato.getElementsByTagName('preco')[0].firstChild.nodeValue
    # calorias = prato.getElementsByTagName('calorias')[0].firstChild.nodeValue
    # tempoP = prato.getElementsByTagName('tempoPreparo')[0].firstChild.nodeValue
    id_ref = id_ref+1

    print(f"{id} - {nome}")

print("-"*30)
campo= int(input("informe o indice:"))
prato = pratos[campo-1]
descricao = prato.getElementsByTagName('descricao')[0].firstChild.nodeValue
ingredientes = prato.getElementsByTagName('ingredientes')[0].firstChild.nodeValue 
preco = prato.getElementsByTagName('preco')[0].firstChild.nodeValue
calorias = prato.getElementsByTagName('calorias')[0].firstChild.nodeValue
tempoP = prato.getElementsByTagName('tempoPreparo')[0].firstChild.nodeValue

print(descricao)

# for prato in pratos:
#     if (campo == id_ref):
#       
#         
#         print(descricao)






    






# print("Olá, bem-vindo(a)!\n Segue a lista dos nossos pratos:")
# pergunta= input(str("Digite o número correspondente ao prato desejado:"))