import requests
from bs4 import BeautifulSoup

from utils.parsing.news import new_article

refer = 'https://stockanalysis.com/stocks/baba/'
html = requests.get(refer)
soup = BeautifulSoup(html.text, 'lxml')

pic = soup.find('div', class_="news-article").find('img').get('src')
link = soup.find('div', class_="news-article").find('h3').find('a').get('href')
title = soup.find('div', class_="news-article").find('h3').find('a').text.strip()
text = soup.find('div', class_="news-article").find('p').text.strip()

The_article = new_article(
    pic=pic,
    link=link,
    title=title,
    text=text
)
