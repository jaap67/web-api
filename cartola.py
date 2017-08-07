import httplib2
import json

def getJogador():
	
	url = ('https://api.cartolafc.globo.com/mercado/destaques')
	h = httplib2.Http()
	response, content = h.request(url, 'GET')
	result = json.loads(content)
	
	atleta = result[0]['Atleta']['nome']
	apelido = result[0]['Atleta']['apelido']
	preco = result[0]['Atleta']['preco_editorial']
	escalacoes = result[0]['escalacoes']
	clube = result[0]['clube']
	posicao = result[0]['posicao']

	return (atleta, apelido, preco, escalacoes, clube, posicao)