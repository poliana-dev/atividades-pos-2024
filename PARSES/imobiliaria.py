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

    imobiliaria.append({
        "Descrição": descricao,
        "Nome": nome_prop,
        "Email": email_prop,
        "Telefone": telefone_prop,
        "Cidade": cidade,
        "Rua": rua,
        "Bairro": bairro,
        "Cidade": cidade,
        "Número de quartos": numQuartos,
        "Número de banheiros": numBanheiros,
        "Tamanho": tamanho,
        "Valor": valor
    })
    
    moveis= imobiliaria

with open ('PARSES/imobiliaria.json', 'w') as json_file:
    json.dump(imobiliaria, json_file,indent=2)

json_string = json.dumps(imobiliaria)
