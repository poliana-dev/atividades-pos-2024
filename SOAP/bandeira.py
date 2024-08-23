import zeep

# define a URL do WSDL
wsdl_url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"

# inicializa o cliente zeep
client = zeep.Client(wsdl=wsdl_url)

# define o código do país para BR
country= str(input("Digite a SIGLA do país (em maiúsculo): "))

# faz a chamada do serviço
result = client.service.CountryFlag(
	sCountryISOCode=country
)
# imprime o resultado
print(f"A bandeira de/o {country} é {result}")
