import requests 
from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.common.proxy import Proxy, ProxyType
from time import sleep 
import configparser
from selenium.webdriver.common.by import By

# proxy = {
#     'http':'http://46.209.49.227:3698',
#     'https':'http://46.209.49.227:3698'
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

# proxy_address = "http://191.102.254.9:8085"

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument(f'--proxy-server={proxy_address}')

#seleniumでブラウザを開く
# driver = webdriver.Chrome(options=chrome_options)

driver = webdriver.Chrome()

url = 'https://gameclub.jp/signin'


# requestsを使用してプロキシを指定したHTTPリクエストを行う
payload = {'api_key': '3309439563baad6898dfd8dde3732678', 'url': 'https://gameclub.jp/signin', 'country_code': 'us', 'device_type': 'desktop'}
response = requests.get('https://api.scraperapi.com/', params=payload)

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
captcha_get = driver.find_element(By.CLASS_NAME,'rc-image-tile-33')['src']

if captcha_get:
    input('手動でcapthca処理をしてください')


driver.quit()




