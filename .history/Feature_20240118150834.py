#自動ログイン、自動出品機能、出品削除機、あらかじめ用意されている画像や文章で出品

from selenium import webdriver 
from time import sleep 

url = 'https://gameclub.jp/gametrade'

driver = webdriver.Chrome()
a = driver.get(url)