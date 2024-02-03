#自動ログイン、自動出品機能、出品削除機、あらかじめ用意されている画像や文章で出品

from selenium import webdriver 
from time import sleep 
from selenium.webdriver.common.by import By

url = 'https://gameclub.jp/gametrade'

driver = webdriver.Chrome()
a = driver.get(url)

driver.implicitly_wait(10)
b = driver.find_element(By.CLASS_NAME,'header-top-btns')
c = b.find_elements(By.TAG_NAME,'a')

for elem in c:
    get_href = elem.get_attribute('href')
    print(i.text)

# b = driver.find_element(By.TAG_NAME,'div')
# driver.implicitly_wait(10)
# c = b.find_element(By.CLASS_NAME,'header-top-btns')
# driver.implicitly_wait(10)
# d = c.find_element(By.TAG_NAME,'a')
# driver.implicitly_wait(10)
# e = d.find_element(By.CLASS_NAME,'btn btn-info')
