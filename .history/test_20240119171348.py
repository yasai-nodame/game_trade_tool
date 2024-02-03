import requests 
from bs4 import BeautifulSoup

# proxy = {
#     'http':'http://110.235.246.220:45212',
#     'https':'http://110.235.246.220:45212'
# }

# try:
#     response = requests.get('https://gameclub.jp/signin',proxies=proxy,timeout=10)
#     response.raise_for_status()
#     print(response.text)
# except requests.exceptions.RequestException as e:
#     print(f'Error:{e}')


payload = { 'api_key': '3309439563baad6898dfd8dde3732678', 'url': 'https://gameclub.jp/signin', 'country_code': 'us', 'device_type': 'desktop' } 
response = requests.get('https://api.scraperapi.com/', params=payload)

soup = BeautifulSoup(response.content,'html.parser')
img_tag = soup.find_all('img')
print(img_tag)
