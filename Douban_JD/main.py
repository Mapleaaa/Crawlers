# -*- coding: utf-8 -*-

import json
import time
import pymongo
import requests
import re
from bs4 import BeautifulSoup


# Create Mongodb Database
# client = pymongo.MongoClient('localhost', 27017)
# douban = client['douban']
# movies = douban['movies']

def get_links_from(pages):
    url = 'https://movie.douban.com/tag/%E6%97%A5%E5%89%A7?start={}&type=S'.format(pages*20)
    wb_data = requests.get(url)
    time.sleep(1)
    soup = BeautifulSoup(wb_data.text, 'lxml')

    titles = soup.select(' td > div > a ')
    links = soup.select('td > div > a')
    points = soup.select(' tr > td > div > div > span.rating_nums')
    infos = soup.select('  tr > td > div > p')

#-*-TEST-*-
    #for link in links:
    #  test = link.get('href')
    #  print(test)

    for title, link, point, info in zip(titles, links, points, infos):
        data = {
            'title': title.get_text().replace("\n", "").replace("\t", "").replace(" ", ""),
            'link': link.get('href'),
            'point': point.get_text(),
            'infos': info.get_text()
        }

        print(data)
       #movies.insert(data)

        with open('process2.json', 'a', encoding='utf-8', errors='ignore') as f:
            encodejson = json.dumps(data, ensure_ascii=False)
            f.write(encodejson)
            f.write('\n')



for page in range(1, 96):
    get_links_from(page)
    print(page)


