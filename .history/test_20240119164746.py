import requests 

proxy = {
    'http':'http://110.235.246.220:45212',
    'https':'http://110.235.246.220:45212'
}

try:
    response = requests.get('https://gameclub.jp/signin',proxies=proxy,timeout=10)
    response.raise_for_status()
    print(response.text)
except requests.exceptions.RequestException as e:
    print(f'Error:{e}')