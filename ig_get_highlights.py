import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from seleniumwire import webdriver as wire_webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests


chrome_options = Options()
driver = wire_webdriver.Chrome(options=chrome_options)
driver.get('http://sssinstagram.com/highlights-downloader')

try:
    btn = driver.find_element(By.CLASS_NAME, 'fc-button-label')
    btn.click()
except:
    pass

try:

    input_field = driver.find_element(By.ID, 'input')
    input_field.send_keys(f'https://www.instagram.com/{sys.argv[1]}')
    input_field.send_keys(Keys.RETURN)
except:
    pass

time.sleep(1)
req = driver.requests
req_url = ''
req_body = ''
req_headers = ''
for request in req:
    if request.response:
        if 'convert' in request.url:
            curl_command = ''
            if request.body:
                req_url = request.url
                req_body = request.body.decode()
                req_headers = request.headers
         
driver.quit()

a = requests.post(req_url, headers=req_headers, data=req_body).json()
for x in a:
    print(x)

