#-*- coding: utf-8 -*-#-*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
newsurl='http://news.sina.com.cn/china/'
res = requests.get(newsurl)
res.encoding='utf-8'
soup = BeautifulSoup(res.text, 'html.parser')
soup.encoding='utf-8'
links = []
links = soup.select("a")
for a in links:
	print(a.text)
	print（a.get("href"))