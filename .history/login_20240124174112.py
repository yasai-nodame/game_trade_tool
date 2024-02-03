import requests 
from selenium import webdriver 
from time import sleep 
import configparser
from selenium.webdriver.common.by import By
import schedule
import time


config = configparser.ConfigParser()
config.read('config.ini',encoding='utf-8')

#ゲームトレードのログインID,PW
login_id = config.get('Credentials','login_id')
login_pw = config.get('Credentials','login_pw')

count = 0

#自動ログインから自動出品までの処理
def execution(): 
    driver = webdriver.Chrome()

    urls = ['https://gameclub.jp/signin','https://gameclub.jp/mypage','https://gameclub.jp/mypage/products/add','https://gameclub.jp/mypage/products']


    # requestsを使用してプロキシを指定したHTTPリクエストを行う
    payload = {'api_key': '3309439563baad6898dfd8dde3732678', 'url': 'https://gameclub.jp/signin', 'country_code': 'us', 'device_type': 'desktop'}
    response = requests.get('https://api.scraperapi.com/', params=payload)

    driver.get(urls[0])
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
    
    #出品してるものを確認し、コメントがついてたらスルーし出品続行、コメントが付いてなかったら出品削除し、出品続行
    sleep(5)
    mypage_menu_get = driver.find_element(By.CLASS_NAME,'side-mypage-menu')
    my_product = mypage_menu_get.find_elements(By.TAG_NAME,'a')[4]
    my_product.click()
    
    #コメントの数字を取得するクラス
    url = urls[3]
    driver.get(url)
    
    # items = driver.find_elements(By.CLASS_NAME,'item')
    
    #countが１以上　つまり１周目以上いってる場合　かつ、リストが空でない場合にのみ処理を実行
    if count:
        items = driver.find_elements(By.CLASS_NAME,'item')
        if items:
            #コメント数を取得
            comment_check = items[2]
            if comment_check == 0:
                selling_exit = driver.find_element(By.CLASS_NAME,'btn btn-danger jsProductClose loader-on-submit')
                selling_exit.click()
    sleep(5)
    
    
    sleep(5)
    
    #ここから出品情報を記載し出品
    exhibit_class = driver.find_element(By.CSS_SELECTOR,'a.btm-add ')
    exhibit_class.click()

    sleep(15)
    
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


execution()



# #20分おきにexecution()を実行
# schedule.every(20).minutes.do(execution)

# while True:
#     schedule.run_pending() #run_pending()でschedule.every(20).minute.do(execution)を実行　しかし20分おき。
#     time.sleep(1)