from xml.dom.minidom import parse

# determio o caminho do arquivo que desejo
caminho = parse("./XML_DTD/atividade01/cardapio.xml")


# 'crio" a raiz
cardapio = caminho.documentElement
pratos= cardapio.getElementsByTagName('prato') #pego o elemento apartir da raiz

print("\nSegue a lista dos nossos pratos:\n")

# determino uma lista
nomes= []
for prato in pratos:
    id = prato.getAttribute('id')
    nome = prato.getElementsByTagName('nome')[0].firstChild.nodeValue
    nomes.append(prato.getElementsByTagName('nome')[0].firstChild.nodeValue) #cada nome é add


    print(f"{id} - {nome}")

print("-"*30)
campo= int(input("informe o indice: "))
print("\n")

# se campo é menor ou igual que a lista dos pratos e dos nome
if  campo <= len(nomes) and 1<=campo<= len(pratos):
    nome = nomes[campo-1] # as listas começam com zero, portanto [campo-1]
    prato = pratos[campo-1]
    descricao = prato.getElementsByTagName('descricao')[0].firstChild.nodeValue
    ingredientes = prato.getElementsByTagName('ingrediente')[0].firstChild.nodeValue 
    preco = prato.getElementsByTagName('preco')[0].firstChild.nodeValue
    calorias = prato.getElementsByTagName('calorias')[0].firstChild.nodeValue
    tempoP = prato.getElementsByTagName('tempoPreparo')[0].firstChild.nodeValue

    print(f"Prato escolhido: {nome}")
    print(f"Descrição: {descricao}\nIngredientes:\n     {ingredientes}\nPreço: {preco}\nCalorias: {calorias}\nTempo de preparo: {tempoP} ")
