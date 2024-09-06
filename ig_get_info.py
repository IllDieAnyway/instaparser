import requests
import sys
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'if-none-match': 'W/"1cc3-JZfCYBSZcvwGoQ2pznH16Gmvoh4"',
    'origin': 'https://storiesig.info',
    'priority': 'u=1, i',
    'referer': 'https://storiesig.info/',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
}

response = requests.get(f'https://api-ig.storiesig.info/api/userInfoByUsername/{sys.argv[1]}', headers=headers).json()

if response:
    resp = response['result']['user']

    username = resp['username'] #Юзернейм
    full_name = resp['full_name'] #Ник
    biography = resp['biography'] #О Себе
    media_count = resp['media_count'] #Статистика/Постов
    follower_count = resp['follower_count']#Статистика/Подписчики
    following_count = resp['following_count'] #Статистика/Подписки
    print(full_name)
