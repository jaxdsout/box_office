import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import requests
from datetime import date


def scrape_box_office(year):
    url = f'https://www.boxofficemojo.com/year/world/{year}/'
    req = requests.get(url)
    content = req.text
    soup = BeautifulSoup(content, features="html.parser")
    rows = soup.findAll('tr')
    appended_data = []

    for index in range(1, len(rows)):
        data_row = {}
        data = rows[index].findAll('td')
        if len(data) == 0:
            continue
        data_row['rank'] = data[0].text
        data_row['title'] = data[1].text
        data_row['worldwide'] = data[2].text
        data_row['domestic'] = data[3].text
        data_row['domestic_pct'] = data[4].text
        data_row['foreign'] = data[5].text
        data_row['foreign_pct'] = data[6].text
        appended_data.append(data_row)

    box_data = pd.DataFrame(appended_data, columns = [
        'rank', 'title', 'worldwide', 'domestic', 'domestic_pct', 'foreign', 'foreign_pct'
    ])
    box_data.to_csv(f'datasets/box_office_{year}.csv', index=False)


current_year = date.today().year
years = range(1977, current_year)
for year in years:
    scrape_box_office(year)
