import requests 
from bs4 import BeautifulSoup 
from useragent_changer import UserAgent

proxy = {
    "http":"89.117.32.209:80",
    "https":"89.117.32.209:80"
}

headers = {
    "User-Agent":"Dalvik/2.1.0 (Linux; U; Android 10; ASUS_Z01RD Build/QKQ1.191008.001)"
}

def get_captcha_image_url():
    url = 'https://gameclub.jp/signin'
    response = requests.get(url,proxies=proxy,headers=headers)
    soup = BeautifulSoup(response.content,'html.parser')
    captcha_image_url = soup
    print(soup.text)
    # <img class="rc-image-tile-33" src="https://www.google.com/recaptcha/api2/payload?p=06AFcWeA5fiNi-U1hP9Rv_URfbwGeTf3e9FPUtCauH6g9TDDcHQfo6KEIfSCUNaGGFQxN7HQhy0X9LsxBR5GNcvj099dZyFhqkE6T3CX2w9tNPkTcLW6rHaFkGwS4KtTgeF9cDOGMgnTUf-MKIzXrQvChF8NA8NdVdrh7c6cvviGLq17V7rF8Lo0d98N43wt6Tgt0DDQ1KUqxdVpN3oKZoMfJSZ0JykEk_eyIgmdjwz3MMuYx5VPpcTNo&amp;k=6LeauPMUAAAAAKGZO3RcZVn3gqnwILzxW2vMTYk4" alt="" style="top:-100%; left: -100%">
    

get_captcha_image_url()