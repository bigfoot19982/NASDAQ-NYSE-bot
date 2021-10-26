import requests
from bs4 import BeautifulSoup


async def get_html(url, header):
    site = requests.get(url, header)
    return site.text


async def get_price(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        price = soup.find('span', class_="text-4xl font-bold").text.strip()
    except:
        price = soup.find('div', class_="block sm:inline text-4xl font-bold").text.strip()
    return price


async def find_value(basic: str, add_to_colon=2, colon=":"):
    return basic.find(colon) + add_to_colon


async def get_indicators(html):
    soup = BeautifulSoup(html, 'lxml')
    trs = list(soup.find('div', class_="order-1 flex flex-row gap-4").find_all('tr'))

    cap = trs[0].get_text(separator=" : ").strip()
    revenue = trs[1].get_text(separator=" : ").strip()
    income = trs[2].get_text(separator=" : ").strip()
    PE = trs[5].get_text(separator=" : ").strip()
    div = trs[7].get_text(separator=" : ").strip()
    target = trs[-2].get_text(separator=" : ").strip()

    indicators = [cap[await find_value(cap):], revenue[await find_value(revenue):], income[await find_value(income):],
                  PE[await find_value(PE):], div[await find_value(div):],
                  target[await find_value(target):]]
    return indicators


async def get_name(html):
    soup = BeautifulSoup(html, 'lxml')
    name = soup.find('h1', class_="text-2xl sm:text-[26px] font-bold text-gray-900").text.strip()
    return name


async def get_html_prof(template):
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'}
    html = requests.get(template + "company/", header)
    return html.text


async def get_picture(template):
    soup = BeautifulSoup(await get_html_prof(template), 'lxml')
    pic = soup.find('img').get('src')
    return pic


async def get_description(template):
    soup = BeautifulSoup(await get_html_prof(template), 'lxml')
    description = soup.find('div', class_="text-page").find('p').text.strip()
    return description


async def getting_info_on_the_ticker(query):
    template = "https://stockanalysis.com/stocks/" + query + "/"
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'}
    html = await get_html(template, header)

    all_data = [await get_name(html), await get_price(html), await get_indicators(html), await get_description(template)]

    try:
        picture = await get_picture(template)
        all_data.append(picture)
    except:
        pass

    return all_data
