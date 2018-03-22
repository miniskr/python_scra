import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.autohome.com.cn/news/')
response.encoding = 'gbk'
soup = BeautifulSoup(response.text, 'html.parser')
#tag = soup.find(id='auto-channel-lazyload-article')
#print(tag)
#h3 = tag.find(name='h3')
li_list = soup.find(id='auto-channel-lazyload-article').find_all(name='li')
#print(li_list)
for li in li_list:
    title = li.find(name='h3')
    if not title:
        continue
    summary = li.find(name='p').text
    #url = li.find('a').attrs['href'] -->字典
    url = li.find('a').get('href')
    img = li.find('a').get('src')

    res = requests.get(img)
    file_name = "%s.jpg" %(title,)
    with open(file_name,'wb') as f:
        f.write(res.content) 