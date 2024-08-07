from xml.dom.minidom import parse
import json


#fazer o mesmo que cardapio mas ter um dict vazio e uma lista vazia.. e depois adcionar as coisas do dict na lista
# e depois fazer as funçoes do json
caminho = parse("./XMLSchema/mobiliaria/imobiliaria.xml")

#raiz do xml
imobiliaria = caminho.documentElement
imoveis= imobiliaria.getElementsByTagName('imovel')

imobiliaria=[]


for imovel in imoveis:
    descricao = imovel.getElementsByTagName('descricao')[0].firstChild.nodeValue
    proprietario = imovel.getElementsByTagName('proprietario')[0].firstChild.nodeValue
    endereco = imovel.getElementsByTagName('endereco')[0].firstChild.nodeValue




#imobilibiaria é a lista de imoveis e os imoveis o dict
