import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.autohome.com.cn/news/')
response.encoding = 'gbk'
soup = BeautifulSoup(response.text, 'html.parser')
tag = soup.find(id='auto-channel-lazyload-article')
#print(tag)
h3 = tag.find(name='h3')
print(h3)