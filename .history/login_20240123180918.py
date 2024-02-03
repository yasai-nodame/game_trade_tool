import requests 
from selenium import webdriver 
from time import sleep 
import configparser
from selenium.webdriver.common.by import By


# proxy = {
#     'http':'http://46.209.49.227:3698',
#     'https':'http://46.209.49.227:3698'
# }

# try:
#     response = requests.get('https://gameclub.jp/signin',proxies=proxy,timeout=10)
#     response.raise_for_status()
#     print(response.text)
# except requests.exceptions.RequestException as e:
#     print(f'Error:{e}')


# payload = { 'api_key': '3309439563baad6898dfd8dde3732678', 'url': 'https://gameclub.jp/signin', 'country_code': 'us', 'device_type': 'desktop' } 
# response = requests.get('https://api.scraperapi.com/', params=payload)

# soup = BeautifulSoup(response.content,'html.parser')
# img_tag = soup.find('div',{'class':'rc-imageselect-challenge'})
# print(img_tag)

config = configparser.ConfigParser()
config.read('config.ini',encoding='utf-8')

#ゲームトレードのログインID,PW
login_id = config.get('Credentials','login_id')
login_pw = config.get('Credentials','login_pw')

# proxy_address = "http://191.102.254.9:8085"

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument(f'--proxy-server={proxy_address}')

#seleniumでブラウザを開く
# driver = webdriver.Chrome(options=chrome_options)

driver = webdriver.Chrome()

urls = ['https://gameclub.jp/signin','https://gameclub.jp/mypage','https://gameclub.jp/mypage/products/add']


# requestsを使用してプロキシを指定したHTTPリクエストを行う
payload = {'api_key': '3309439563baad6898dfd8dde3732678', 'url': 'https://gameclub.jp/signin', 'country_code': 'us', 'device_type': 'desktop'}
response = requests.get('https://api.scraperapi.com/', params=payload)

a = driver.get(urls[0])
login_email_get = driver.find_element(By.CLASS_NAME,'email')
login_password_get = driver.find_element(By.CLASS_NAME,'password')

login_email_get.send_keys(login_id)
sleep(20)
login_password_get.send_keys(login_pw)

sleep(20)
#私はロボットではありませんをFullXpathでチェックさせる
checkbox = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[2]/div[1]/form/div[1]/div')
sleep(20)
checkbox.click()
sleep(20)
# WebDriverWait(driver,10).until(
#     EC.presence_of_all_elements_located((By.ID,'rc-imageselect-target'))
# )
# captcha_get = driver.find_element(By.ID,'rc-imageselect-target')
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

url = urls[1]

driver.get(url)

exhibit_class = driver.find_element(By.CSS_SELECTOR,'a.btm-add ')
exhibit_class.click()

sleep(15)

#ここから出品情報を記載し出品

url = urls[2]
exhibit_title = config.get('Credentials','exhibit_title')
product_description = config.get('Credentials','product_description')
product_price = config.get('Credentials','product_price')


driver.get(url)
sleep(10)
game_title_id = driver.find_element(By.ID,'btn-search-title')
game_title_id.click()
sleep(10)
game_title_span = driver.find_element(By.CSS_SELECTOR,'span.title-name') #選択したゲームタイトルを選択
game_title_span.click()

sleep(10)
radio_choice = driver.find_element(By.ID,'account-type-id-10')
radio_choice.click() #ラジオボタンクリック

exhibit_title_name = driver.find_element(By.ID,'name')
exhibit_title_name.send_keys(exhibit_title) #商品タイトル入力
sleep(10)

product_discription_id = driver.find_element(By.ID,'input-body-text')
product_discription_id.send_keys(product_description) #商品説明入力
sleep(10)
product_price_class = driver.find_element(By.CLASS_NAME,'price')
product_price_class.send_keys(product_price) #価格入力
sleep(10)
confirm_id = driver.find_element(By.ID,'btn-confirm')
confirm_id.click()
sleep(10)

exhibit_decision = driver.find_element(By.ID,'btn-add')
exhibit_decision.click()

sleep(15)