# 23
import requests
from bs4 import BeautifulSoup
url = 'https://www.example.com'  # 网页地址
response = requests.get(url)
html = response.text  # 获取网页内容
soup = BeautifulSoup(html, 'html.parser')
img_tags = soup.find_all('img')
img_urls = [img['src'] for img in img_tags]
for url in img_urls:    
    response = requests.get(url)    
    with open('photo.jpg', 'wb') as f:        
         f.write(response.content)
