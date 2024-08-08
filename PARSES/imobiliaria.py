from xml.dom.minidom import parse
import json

caminho = parse("./XMLSchema/mobiliaria/imobiliaria.xml")

#raiz do xml
imobiliaria = caminho.documentElement
imoveis= imobiliaria.getElementsByTagName('imovel')

imobiliaria=[]
moveis = {}


for imovel in imoveis:
    descricao = imovel.getElementsByTagName('descricao')[0].firstChild.nodeValue
    nome_prop = imovel.getElementsByTagName('nome')[0].firstChild.nodeValue
    email_prop =  imovel.getElementsByTagName('email')[0].firstChild.nodeValue
    telefone_prop = imovel.getElementsByTagName('telefone')[0].firstChild.nodeValue

    # endereço
    rua = imovel.getElementsByTagName('rua')[0].firstChild.nodeValue
    bairro = imovel.getElementsByTagName('bairro')[0].firstChild.nodeValue
    cidade = imovel.getElementsByTagName('cidade')[0].firstChild.nodeValue

    numQuartos = imovel.getElementsByTagName('numQuartos')[0].firstChild.nodeValue
    numBanheiros = imovel.getElementsByTagName('numBanheiros')[0].firstChild.nodeValue
    tamanho = imovel.getElementsByTagName('tamanho')[0].firstChild.nodeValue

    valor = imovel.getElementsByTagName('valor')[0].firstChild.nodeValue

    imobiliaria.append(descricao)
    imobiliaria.append(nome_prop)
    imobiliaria.append(email_prop)
    imobiliaria.append(telefone_prop)
    imobiliaria.append(rua)
    imobiliaria.append(bairro)
    imobiliaria.append(cidade)
    imobiliaria.append(numQuartos)
    imobiliaria.append(numBanheiros)
    imobiliaria.append(tamanho)
    imobiliaria.append(valor)
    
    moveis= imobiliaria

# with open ('imobiliaria.json', 'w') as json_file:
#     json.dump(moveis, json_file,indent=2)

# json_string = json.dumps(moveis)
