import requests 
from selenium import webdriver 
from time import sleep 
import configparser
from selenium.webdriver.common.by import By
import schedule
import time

url = 'https://gameclub.jp/mypage/products'
driver = webdriver.Chrome()

payload = { 'api_key': '3309439563baad6898dfd8dde3732678', 'url': 'https://gameclub.jp/mypage/products', 'render': True, 'device_type': 'desktop', 'country_code': 'us' } 
r = requests.get('https://api.scraperapi.com/', params=payload)


driver.get(url)

sleep(5)