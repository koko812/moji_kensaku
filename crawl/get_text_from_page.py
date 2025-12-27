import requests
from bs4 import BeautifulSoup as bs
from collections import Counter
from urllib.parse import urljoin
import os
import zipfile

url = "https://www.aozora.gr.jp/cards/000148/card50420.html"
response = requests.get(url)
response.encoding = 'utf-8'

parsed = bs(response.text, "html.parser")
all_elems = parsed.find_all(True)
all_elems_list = [n.name for n in all_elems]
tags = set(all_elems_list)
tags_counts = Counter(all_elems_list)
print(tags)
print(tags_counts)

tables = parsed.find_all("table")
print(len(tables))
print(tables[-1].find_all("a"))
a_s = tables[-1].find_all("a")
r_link = a_s[-2].get("href")
print(r_link)

link = urljoin(url, r_link)
print(link)
zip_resp = requests.get(link)
print(dir(zip_resp))
print(zip_resp.json)
print(zip_resp.headers)
#print(zip_resp.content)

rest_dir = 'datas'
os.makedirs(rest_dir, exist_ok=True)
dist_path = os.path.join(rest_dir, os.path.basename(r_link))
with open(dist_path, "wb") as f:
    f.write(zip_resp.content)

with open(dist_path.split('.')[0]+'.txt', 'wt') as f:
    with open(dist_path, 'rb') as g:
        txt_data = zipfile.ZipFile(g)
        print(txt_data)
        name = txt_data.namelist()[0]
        txt = txt_data.read(name).decode("shift_jis", errors="ignore")
    f.write(txt)

