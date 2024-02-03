import requests 

import requests

payload = { 'api_key': '3309439563baad6898dfd8dde3732678', 'url': 'https://gameclub.jp/signin', 'render': True, 'country_code': 'us', 'device_type': 'desktop' } 
r = requests.get('https://api.scraperapi.com/', params=payload)


data = r.json()

print(data)
