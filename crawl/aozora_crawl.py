import requests
from bs4 import BeautifulSoup as bs
from collections import Counter

url = "https://www.aozora.gr.jp/"
req = requests.get(url=url)
req.encoding = 'utf-8'
print(dir(req))
print(req.status_code, req.url)
text = req.text

parsed = bs(text, "html.parser")
print(dir(parsed))

print(parsed.title)
print(type(parsed.find_all(True)[0].name))
print(parsed.find_all(True)[0].name)
print(parsed.find_all(True)[1].name)
print(parsed.find_all(True)[1].name)
tags = [tag.name for tag in parsed.find_all(True)]
print(Counter(tags))

print(len(parsed.find_all("table")))
print(req.apparent_encoding)

tables = parsed.find_all("table")
elem = [table.find(string=lambda s: s and "公開中" in s) for table in tables]
print(len(elem))

elem = parsed.find_all(string=lambda s: s and "公開中" in s) 
print(elem, len(elem), type(elem))
sakkabetu = elem[1]
print(type(sakkabetu))
print(sakkabetu)
print(len(sakkabetu.find_parent("table")))
print(dir(sakkabetu.find_parent("table")))
print(sakkabetu.find_parent("tr").text)
print(sakkabetu.find_parent("tr"))