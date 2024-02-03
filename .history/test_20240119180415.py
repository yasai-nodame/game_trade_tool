import requests 
from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.common.proxy import Proxy, ProxyType
from time import sleep 
import configparser
from selenium.webdriver.common.by import By

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

config = configparser.ConfigParser()
config.read('config.ini')

#ゲームトレードのログインID,PW
login_id = config.get('Credentials','login_id')
login_pw = config.get('Credentials','login_pw')

proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = "http://191.102.254.9:8085"
proxy.ssl_proxy = "https://191.102.254.9:8085"


#プロキシをブラウザに適用
capabilities = webdriver.DesiredCapabilities.CHROME
proxy.add_to_capabilities(capabilities)

#seleniumでブラウザを開く
driver = webdriver.Chrome(desired_capabilities=capabilities)

url = 'https://gameclub.jp/signin'

a = driver.get(url)
login_email_get = driver.find_element(By.CLASS_NAME,'email')
login_password_get = driver.find_element(By.CLASS_NAME,'password')

login_email_get.send_keys(login_id)
sleep(20)
login_password_get.send_keys(login_pw)

sleep(20)
#私はロボットではありませんをFullXpathでチェックさせる
checkbox = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[2]/div[1]/form/div[1]/div')
sleep(20)
checkbox.click()
sleep(20)
driver.quit()

# requestsを使用してプロキシを指定したHTTPリクエストを行う
payload = {'api_key': '3309439563baad6898dfd8dde3732678', 'url': 'https://gameclub.jp/signin', 'country_code': 'us', 'device_type': 'desktop'}
response = requests.get('https://api.scraperapi.com/', params=payload, proxies={"http": "http://your_proxy_address", "https": "https://your_proxy_address"})


