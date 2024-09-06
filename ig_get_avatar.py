import requests
from bs4 import BeautifulSoup
import sys

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://indownloader.app',
    'Referer': 'https://indownloader.app/instagram-profile-viewer',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = {
    'link': f'https://www.instagram.com/{sys.argv[1]}',
    'downloader': 'avatar',
}

response = requests.post('https://indownloader.app/request', headers=headers, data=data)
html_content = response.content
soup = BeautifulSoup(html_content, "html.parser")

# Find all the <a> tags with the 'href' attribute
links = soup.find_all("a", href=True)

# Extract the href URLs
href_urls = [link["href"] for link in links]
urls = []
for url in href_urls:
    url = url.replace('\"', '').replace('\\', '')
    urls.append(url)

avatar = urls[0]
print(avatar)
