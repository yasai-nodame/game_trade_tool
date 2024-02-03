import requests 
from selenium import webdriver 
from time import sleep 
import configparser
from selenium.webdriver.common.by import By
import schedule
import time

config = configparser.ConfigParser()
config.read('config.ini',encoding='utf-8')

#ゲームトレードのログインID,PW
login_id = config.get('Credentials','login_id')
login_pw = config.get('Credentials','login_pw')

url = 'https://gameclub.jp/mypage/products'
driver = webdriver.Chrome()

payload = { 'api_key': '3309439563baad6898dfd8dde3732678', 'url': 'https://gameclub.jp/mypage/products', 'render': True, 'device_type': 'desktop', 'country_code': 'us' } 
r = requests.get('https://api.scraperapi.com/', params=payload)

driver.get(url)
sleep(5)
login_email_get = driver.find_element(By.CLASS_NAME,'email')
login_password_get = driver.find_element(By.CLASS_NAME,'password')

login_email_get.send_keys(login_id)
sleep(20)
login_password_get.send_keys(login_pw)

sleep(20)
#私はロボットではありませんをFullXpathでチェックさせる
# checkbox = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[2]/div[1]/form/div[1]/div')
checkbox = driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div[1]/div/div/span/div[2]')
sleep(20)
checkbox.click()
sleep(20)
iframe_element = driver.find_element(By.TAG_NAME,'iframe')

driver.switch_to.frame(iframe_element)

if iframe_element:
    input('captchaが表示されたので手動で解決してください。 終わったらEnterを押してください。 また自動処理を行います。')
    
driver.switch_to.default_content()
sleep(20)
#ログインクリックを自動処理
login_button = driver.find_element(By.TAG_NAME,'button')
login_button.click()

sleep(10)