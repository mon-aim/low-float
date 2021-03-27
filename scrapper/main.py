import json
import re
from datetime import datetime
from typing import List

import requests
from bs4 import BeautifulSoup
from bs4.element import Tag


HOST = 'https://www.lowfloat.com'
HEADERS = {
    "Host": f"{HOST}",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
    "Upgrade-Insecure-Requests": "1",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
}


def scrape_info():
    response = requests.get(HOST, HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')

    tables: List[Tag] = soup.find_all('table')

    info = {}

    last_update = tables[0].find_all('tr')[-1].text
    last_update = re.search(r'on\s(.+)', last_update).group(1)
    info['last_update'] = datetime.strptime(last_update, '%B %d, %Y').__str__()

    all_stocks = tables[0].find('p', {'class': 'nav'}).text
    info['all_stocks'] = int(re.search(r'of\s(\d+)\s', all_stocks).group(1))

    return info


def scrape_table(page):
    response = requests.get(f'{HOST}/all/{page}', HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')
    tables: List[Tag] = soup.find_all('table')
    table = tables[2]

    header = table.find_all('tr')[0].find_all('td')
    header = list(map(lambda x: x.text.strip(), header))

    trs = table.find_all('tr')

    return [dict(zip(header, [td.text.strip() for td in tds])) for index, tr in enumerate(trs) if index > 0 and len(tds := tr.find_all('td')) > 1]


def main():

    info = scrape_info()

    with open(f'scrape.json', 'w') as f:
        for i in range(1, 2):
            json.dump({'data': scrape_table(i), **info}, f, indent=4)


if __name__ == '__main__':
    main()
