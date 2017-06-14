#function that access API 
import sys
import requests

url = 'http://api.fixer.io/latest'
base_currencies = ['GBP','USD','CAD']
rate_in = 'CAD'

def get_exchange_rates(currency,rate_in):
	query = url +'?base=%s&symbols=%s'%(currency,rate_in)
	try:
		response = requests.get(query)
		if response.status_code != 200:
			response = 'N/A'
			return response
		else:
			rates = response.json()
			rate_in_currency = rates['rates'][rate_in]
			return rate_in_currency
	except requests.ConnectionError as error:
		print error
		sys.exit(1)

def main():
	for currency in base_currencies:
		rate = get_exchange_rates(currency,rate_in)
		print currency, rate

if __name__ == '__main__':
	main()



	
