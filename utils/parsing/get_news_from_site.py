import requests
from bs4 import BeautifulSoup

from handlers.users.supplementary.get_indexes import indexes

# a class for better representation of parsed info
class new_article:
    def __init__(self, pic, link, title, text):
        self.pic = pic
        self.link = link
        self.title = title
        self.text = text


async def check_on_company_site(s: str):
    # getting company name from Record (str)
    positions_in_company_name = await indexes('\'', '\'', s, 1)
    company = s[positions_in_company_name[0]:positions_in_company_name[1]].lower()

    refer = 'https://stockanalysis.com/stocks/' + company + '/'

    html = requests.get(refer)
    soup = BeautifulSoup(html.text, 'lxml')

    pic = soup.find('div', class_="news-article").find('img').get('src')
    link = soup.find('div', class_="news-article").find('h3').find('a').get('href')
    title = soup.find('div', class_="news-article").find('h3').find('a').text.strip()
    text = soup.find('div', class_="news-article").find('p').text.strip()

    # form new entity of new_article class using the data we've parsed while searching news
    The_article = new_article(pic, link, title, text)
    # we use link to the news as the hash
    new_hash = The_article.link

    return The_article, new_hash, company
