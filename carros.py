import httplib2
import json

def carros():
	
	url = ('https://fipe-parallelum.rhcloud.com/api/v1/carros/marcas')
	h = httplib2.Http()
	response, content = h.request(url, 'GET')
	result = json.loads(content)

	carronome = result[0]['nome']
	carrocodigo = result[0]['codigo']
	carronome1 = result[1]['nome']
	carrocodigo1 = result[1]['codigo']
	
	return (carronome, carrocodigo, carronome1, carrocodigo1)