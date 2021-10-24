from dataclasses import dataclass

import requests
from bs4 import BeautifulSoup


@dataclass
class new_article:
    def __init__(self, pic, link, title, text):
        self.pic = pic
        self.link = link
        self.title = title
        self.text = text


async def check_if_news(s: str):
    name_first = s.find('\'') + 1
    name_last = s.find('\'', name_first)

    company = s[name_first:name_last].lower()

    refer = 'https://stockanalysis.com/stocks/' + company + '/'

    html = requests.get(refer)
    soup = BeautifulSoup(html.text, 'lxml')

    pic = soup.find('div', class_="news-article").find('img').get('src')
    link = soup.find('div', class_="news-article").find('h3').find('a').get('href')
    title = soup.find('div', class_="news-article").find('h3').find('a').text.strip()
    text = soup.find('div', class_="news-article").find('p').text.strip()

    The_article = new_article(pic, link, title, text)

    new_hash = The_article.link

    return The_article, new_hash, company
