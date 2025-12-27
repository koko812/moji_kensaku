# このセッションで学んだこと

## requests の疎通確認
- `get()` で取得して `status_code` と `text` を確認する
- 本文は先頭だけ見ると安全

```python
r = requests.get(url)
print(r.status_code)
print(r.text[:200])
```

## BeautifulSoup の基本フロー
- HTML取得 → 文字コード確認 → パース → find/select で抽出
- `apparent_encoding` に合わせると文字化けしにくい

```python
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text, "html.parser")
```

## パーサ名の指定
- 正しい名前は `"html.parser"`
- `"html_parser"` は `FeatureNotFound` になる
- 別パーサなら `"lxml"`

```python
BeautifulSoup(html, "html.parser")
```

## タグ一覧の取得
- `find_all(True)` で全タグを列挙して集計

```python
tags = [t.name for t in soup.find_all(True)]
print(sorted(set(tags)))
```

## 文字列検索（完全一致・部分一致）
- 完全一致は `string="..."` を使う
- 部分一致は関数で条件を書く

```python
soup.find(string="公開中　作家別：")
soup.find(string=lambda s: s and "公開中" in s and "作品別" in s)
```

## find_all と find の違い
- `find_all` はリスト（ResultSet）を返す
- そのまま `find` は使えないので各要素に対して探す

```python
tables = soup.find_all("table")
for t in tables:
    hit = t.find(string=lambda s: s and "公開中" in s)
    if hit:
        target = t
        break
```

## 相対URLの絶対化（urljoin）
- `urljoin(基準URL, 相対URL)` で合成

```python
from urllib.parse import urljoin
abs_url = urljoin("https://www.aozora.gr.jp/cards/000081/", "./files/xxx.zip")
```

## href からファイル名を取る
- 末尾の basename を使う

```python
from pathlib import PurePosixPath
name = PurePosixPath(href).name
```

## zip の読み取り
- zip はバイナリ（`response.content`）として扱う
- `ZipFile` で中身を読む

```python
from io import BytesIO
from zipfile import ZipFile

z = ZipFile(BytesIO(response.content))
name = z.namelist()[0]
data = z.read(name)
```

## Shift_JIS でのデコード
- 青空文庫は Shift_JIS が多い
- 読めない文字は `errors="ignore"` で回避

```python
text = data.decode("shift_jis", errors="ignore")
```
