#自動ログイン、自動出品機能、出品削除機、あらかじめ用意されている画像や文章で出品

from selenium import webdriver 
from time import sleep 
from selenium.webdriver.common.by import By
import configparser 

config = configparser.ConfigParser()
config.read('config.ini')

#ゲームトレードのログインID,PW
login_id = config.get('Credentials','login_id')
login_pw = config.get('Credentials','login_pw')

#ゲームトレードのサイトURL
url = ['https://gameclub.jp/gametrade','https://gameclub.jp/signin']

driver = webdriver.Chrome()
web_url = driver.get(url[0])

driver.implicitly_wait(5)
#ヘッダーにある新着情報、会員登録、ログインのクラスを取得
login_class_get = driver.find_element(By.CLASS_NAME,'header-top-btns')
driver.implicitly_wait(5)

#ログインのhrefを取得する
login_tag_get = login_class_get.find_elements(By.TAG_NAME,'a')
driver.implicitly_wait(5)
#ログインをクリックする
login_tag_get[2].click()

driver.get(url[1])
driver.implicitly_wait(5)
login_email_get = driver.find_element(By.CLASS_NAME,'email')
login_password_get = driver.find_element(By.CLASS_NAME,'password')

driver.implicitly_wait(5)
login_email_get.send_keys(login_id)
driver.implicitly_wait(5)
login_password_get.send_keys(login_pw)

checkbox = driver.find_element(By.XPATH,'//*[@id="recaptcha-anchor"]/div[1]')
checkbox.click()

# for elem in c:
#     get_href = elem.get_attribute('href')
#     print(get_href)

# b = driver.find_element(By.TAG_NAME,'div')
# driver.implicitly_wait(10)
# c = b.find_element(By.CLASS_NAME,'header-top-btns')
# driver.implicitly_wait(10)
# d = c.find_element(By.TAG_NAME,'a')
# driver.implicitly_wait(10)
# e = d.find_element(By.CLASS_NAME,'btn btn-info')
