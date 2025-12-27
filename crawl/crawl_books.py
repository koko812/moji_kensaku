import requests
from bs4 import BeautifulSoup as bs
from collections import Counter
from urllib.parse import urljoin

def get_and_parse(url):
    req = requests.get(url)
    req.encoding="utf-8"
    return bs(req.text, "html.parser")

base_url = "https://www.aozora.gr.jp/"
parsed = get_and_parse(base_url)

tables = list(parsed.find_all("table"))
indices_table = [tabl for tabl in tables if tabl.find(string="メインエリア")][0]
trs = list(indices_table.find_all("tr"))
#print(trs)
sakka_tr = [tr for tr in trs if tr.find(string=lambda s:s and "作家別" in s)][0]
a_s = list(sakka_tr.find_all("a"))
links = [a.get("href") for a in a_s]

url = urljoin(base_url, links[4])
parsed = get_and_parse(url)

a_s = [a for li in parsed.find_all("li") for a in li.find_all("a", href=True)]
#print(a_s)
#print(type(a_s[0]))
natume_link = [a.get('href') for a in a_s if a.find_all(string=lambda s:s and "夏目" in s)][0]
#print(natume_link)

natume_parsed = get_and_parse(urljoin(url, natume_link))
#print(natume_parsed)
books = list(natume_parsed.find_all("ol"))[0]
print(books)

links = [a.get("href") for a in books.find_all("a", href=True)]
print(links)

link = links[0]
book_page = get_and_parse(urljoin(url, link))
print(book_page)

