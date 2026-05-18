#3주차
#  # # import pandas as pd

# # # sales = pd.DataFrame({
# # #     'name': ['사과','딸기','수박'],
# # #     'price': [1800,1500,3000],
# # #    'value':[24,38,13]
# # # })
# # # print(sales)

# # # print(sum(sales['price'])/3)
# # # print(sum(sales['value'])/3)

# # # import pandas as pd

# # # mpg = pd.read_csv('mpg.csv')
# # # mpg_new=mpg.copy()

# # # mpg_new = mpg_new.rename(columns={'cty':'city'})
# # # mpg_new = mpg_new.rename(columns={'hwy':'hiway'})

# # # print(mpg_new.head())

# # import pandas as pd

# # mpg = pd.read_csv('mpg.csv')

# # print(
# #     mpg.query('manufacturer == "audi"')
# #        .sort_values('hwy', ascending=False)
# #        .head()
# # )

# import pandas as pd

# mpg = pd.read_csv('mpg.csv')

# mpg_a = mpg.query('displ <= 4')
# mpg_b = mpg.query('displ >= 5')
# print(mpg_a['hwy'].mean())
# print(mpg_b['hwy'].mean())

# mpg_audi = mpg.query('manufacturer == "audi"')
# mpg_toyota = mpg.query('manufacturer == "toyota"')
# print(mpg_audi['cty'].mean())
# print(mpg_toyota['cty'].mean())

# mpg_new = mpg.query('manufacturer in ["chevrolet", "ford", "honda"]')
# print(mpg_new['hwy'].mean())

# import pandas as pd

# mpg = pd.read_csv('mpg.csv')

# mpg_new = mpg.copy()
# mpg_new = mpg_new.assign(total = mpg_new['cty'] + mpg_new['hwy'])

# mpg_new = mpg_new.assign(mean = mpg_new['total'] / 2)

# print(mpg_new.sort_values('mean', ascending=False).head(3))

#4주차
#import requests
# from bs4 import BeautifulSoup

# soup= BeautifulSoup (requests.get('https://quotes.toscrape.com/').text,'lxml')

# for i in soup.find_all('div', {'class': 'quote'}):
# print(i.text)

import os, re, requests
from bs4 import BeautifulSoup

os.makedirs("Crawling", exist_ok=True)
news = 'https://news.daum.net/climate'
res = requests.get(news)
res.encoding = 'utf-8'

soup = BeautifulSoup(res.text, 'lxml')


for i in soup.find_all('div', {'class': 'cont_thumb'}):
    print(i.text)

for i in soup.find_all('div', {'class': 'cont_thumb'}):
    print(i.find_parent('a').get('href'))

article = "https://v.daum.net/v/20260323113002206"

res = requests.get(article)
res.encoding = "utf-8"

soup2 = BeautifulSoup(res.text, "lxml")

for i in soup2.find_all("p"):
    print(i.text)

from datetime import datetime
import os
import requests
from bs4 import BeautifulSoup

today = datetime.now().strftime("%Y%m%d")
file_path = os.path.join("Crawling", today + ".txt")

with open(file_path, "w", encoding="utf-8") as f:
    for i in soup.find_all("div", {"class": "cont_thumb"}):
        link = i.find_parent("a").get("href")

        title_tag = i.find("strong", class_="tit_txt")
        if not title_tag:
            continue
        title = title_tag.get_text(strip=True)

        sub_res = requests.get(link)
        sub_res.encoding = "utf-8"
        sub_soup = BeautifulSoup(sub_res.text, "lxml")

        content = sub_soup.find("div", {"class": "article_view"})
        if content:
            article_text = content.get_text("\n", strip=True)
        else:
            article_text = "본문 없음"

        f.write(title + "\n")
        f.write(link + "\n")
        f.write(article_text + "\n")
        f.write("-" * 50 + "\n")

print(f"저장 완료: {file_path}")