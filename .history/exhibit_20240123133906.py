import requests 
from selenium import webdriver 
from time import sleep 
import configparser
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = 'https://gameclub.jp/mypage/products/add'

# requestsを使用してプロキシを指定したHTTPリクエストを行う
payload = { 'api_key': '3309439563baad6898dfd8dde3732678', 'url': 'https://gameclub.jp/mypage/products/add' } 
r = requests.get('https://api.scraperapi.com/', params=payload)


sleep(10)
