#自動ログイン、自動出品機能、出品削除機、あらかじめ用意されている画像や文章で出品

from selenium import webdriver 
from time import sleep 
from selenium.webdriver.common.by import By

url = 'https://gameclub.jp/gametrade'

driver = webdriver.Chrome()
a = driver.get(url)

b = driver.find_element(By.CLASS_NAME,'btn btn-info')
b.click()