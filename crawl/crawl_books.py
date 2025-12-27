import requests
from bs4 import BeautifulSoup as bs
from collections import Counter

url = "https://www.aozora.gr.jp/"
req = requests.get(url=url)
req.encoding = 'utf-8'
text = req.text
parsed = bs(text, "html.parser")

tables = parsed.find_all("table")

elem = parsed.find_all(string=lambda s: s and "公開中" in s) 
sakkabetu = elem[1]

print(sakkabetu)