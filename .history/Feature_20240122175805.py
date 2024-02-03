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

sleep(20)#ヘッダーにある新着情報、会員登録、ログインのクラスを取得
login_class_get = driver.find_element(By.CLASS_NAME,'header-top-btns')
sleep(20)
#ログインのhrefを取得する
login_tag_get = login_class_get.find_elements(By.TAG_NAME,'a')
sleep(20)#ログインをクリックする
login_tag_get[2].click()

driver.get(url[1])
sleep(20)
login_email_get = driver.find_element(By.CLASS_NAME,'email')
login_password_get = driver.find_element(By.CLASS_NAME,'password')

sleep(20)
login_email_get.send_keys(login_id)
sleep(20)
login_password_get.send_keys(login_pw)
sleep(20)
#私はロボットではありませんをFullXpathでチェックさせる
checkbox = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[2]/div[1]/form/div[1]/div')
sleep(60)
checkbox.click()
sleep(60)

login_click = driver.find_element(By.CLASS_NAME,'btn btn-danger btn-registration')

login_click.click()

# for elem in c:
#     get_href = elem.get_attribute('href')
#     print(get_href)

# b = driver.find_element(By.TAG_NAME,'div')
# sleep(60)# c = b.find_element(By.CLASS_NAME,'header-top-btns')
# sleep(60)# d = c.find_element(By.TAG_NAME,'a')
# sleep(60)# e = d.find_element(By.CLASS_NAME,'btn btn-info')

