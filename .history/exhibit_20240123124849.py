import requests 
from selenium import webdriver 
from time import sleep 
import configparser
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = 'https://gameclub.jp/'

# requestsを使用してプロキシを指定したHTTPリクエストを行う
payload = {'api_key': '3309439563baad6898dfd8dde3732678', 'url': 'https://gameclub.jp/signin', 'country_code': 'us', 'device_type': 'desktop'}
response = requests.get('https://api.scraperapi.com/', params=payload)

driver.get(url)

sleep(10)
exhibit_button = driver.find_element(By.CLASS_NAME,'btm-add')
sleep(10)
exhibit_button_link = exhibit_button.find_element(By.TAG_NAME,'a')
sleep(10)
# exhibit_button_link.click()
print(exhibit_button_link)
