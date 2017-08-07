import httplib2
import json

def coinDesk():
	
	url = ('https://api.coindesk.com/v1/bpi/currentprice.json')
	h = httplib2.Http()
	response, content = h.request(url, 'GET')
	result = json.loads(content)

	time = result['time']['updated']
	name = result['chartName']
	usscode = result['bpi']['USD']['code']
	usssymbol = result['bpi']['USD']['symbol']
	ussrate = result['bpi']['USD']['rate']
	ussdescription = result['bpi']['USD']['description']
	ussratefloat = result['bpi']['USD']['rate_float']

	return (time, name, usscode, usssymbol, ussrate, ussdescription, ussratefloat)