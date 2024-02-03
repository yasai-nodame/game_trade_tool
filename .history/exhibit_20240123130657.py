import requests 
from selenium import webdriver 
from time import sleep 
import configparser
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = 'https://gameclub.jp/mypage/products/add'

# requestsを使用してプロキシを指定したHTTPリクエストを行う
payload = {'api_key': '3309439563baad6898dfd8dde3732678', 'url': 'https://gameclub.jp/signin', 'country_code': 'us', 'device_type': 'desktop'}
response = requests.get('https://api.scraperapi.com/', params=payload)


driver.get(url)

a = driver.find_element(By.ID,'btn-search-title')
a.click()