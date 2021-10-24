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


async def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    trs = list(soup.find('div', class_="order-1 flex flex-row gap-4").find_all('tr'))

    cap = trs[0].get_text(separator=" : ").strip()
    revenue = trs[1].get_text(separator=" : ").strip()
    income = trs[2].get_text(separator=" : ").strip()
    PE = trs[5].get_text(separator=" : ").strip()
    div = trs[7].get_text(separator=" : ").strip()
    target = trs[-2].get_text(separator=" : ").strip()

    c_cap = cap.find(":")
    c_rev = revenue.find(":")
    c_inc = income.find(":")
    c_pe = PE.find(":")
    c_div = div.find(":")
    c_targ = target.find(":")

    indicators = [cap[c_cap + 2:], revenue[c_rev + 2:], income[c_inc + 2:], PE[c_pe + 2:], div[c_div + 2:],
                  target[c_targ + 2:]]
    return indicators


async def get_name(html):
    soup = BeautifulSoup(html, 'lxml')
    name = soup.find('h1', class_="text-2xl sm:text-[26px] font-bold text-gray-900").text.strip()
    return name


async def get_ownership(query):
    url_1 = "https://finance.yahoo.com/quote/"
    url_2 = "/holders?p="
    common_url = url_1 + query + url_2 + query
    print(common_url)
    site = requests.get(common_url).text
    print(site)
    soup = BeautifulSoup(site, 'lxml')
    print(soup)
    ownership = soup.find('div', class_="W(100%) Mb(20px)").find('tr', classs_="BdT Bdc($seperatorColor)").text.strip()
    print(ownership)
    return ownership


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


async def func(query):
    template = "https://stockanalysis.com/stocks/" + query + "/"
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'}
    html = await get_html(template, header)
    all_data = []
    name = await get_name(html)
    price = await get_price(html)
    indicators = await get_data(html)
    all_data.append(price)
    all_data.append(indicators)
    all_data.append(name)
    # ownership = await get_ownership(query)
    try:
        picture = await get_picture(template)
        all_data.append(picture)
    except:
        pass
    description = await get_description(template)
    all_data.append(description)

    return all_data
