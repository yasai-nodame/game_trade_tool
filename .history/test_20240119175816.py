import requests 
from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.common.proxy import Proxy, ProxyType

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


# payload = { 'api_key': '3309439563baad6898dfd8dde3732678', 'url': 'https://gameclub.jp/signin', 'country_code': 'us', 'device_type': 'desktop' } 
# response = requests.get('https://api.scraperapi.com/', params=payload)

# soup = BeautifulSoup(response.content,'html.parser')
# img_tag = soup.find('div',{'class':'rc-imageselect-challenge'})
# print(img_tag)

proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = "http://191.102.254.9:8085"
proxy.ssl_proxy = "https://191.102.254.9:8085"


#プロキシをブラウザに適用
capabilities = webdriver.DesiredCapabilities.CHROME
proxy.add_to_capabilities(capabilities)

#seleniumでブラウザを開く
driver = webdriver.Chrome(desired_capabilities=capabilities)

driver.quit()

# requestsを使用してプロキシを指定したHTTPリクエストを行う
payload = {'api_key': '3309439563baad6898dfd8dde3732678', 'url': 'https://gameclub.jp/signin', 'country_code': 'us', 'device_type': 'desktop'}
response = requests.get('https://api.scraperapi.com/', params=payload, proxies={"http": "http://your_proxy_address", "https": "https://your_proxy_address"})


