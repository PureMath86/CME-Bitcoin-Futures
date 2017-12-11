from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
from datetime import datetime as dt
from pprint import pprint
#%pprint

TEN_MIN = 10*60.0

class RequestSoup_spider():

    def __init__(self, url):
        self.url = url
        self.s = requests.Session()
        self.s.headers.update({'User-Agent': 'CME_Python'})
        self.r = self.s.get(self.url)
        self.data = self.r.text
        self.soup = BeautifulSoup(self.data, "html.parser")

    def list_data(self, tag):
        self._list = []
        for item in self.soup.find_all(tag):
            self._list.append(item.contents)

        return self._list

time.sleep(0.1)

dt.now()

url = r"http://www.cmegroup.com/trading/equity-index/us-index/bitcoin.html"

spider = RequestSoup_spider(url)

pprint(spider.s.headers)

pd.read_html(spider.data, header=0)[0]

table = spider.soup.find_all('table')[0]
rows = table.find_all('tr')

t_list = []
for row in rows:
    c_list = []
    cols = row.find_all('td')
    for col in cols:
        c_list.append(col.text)
    t_list.append(c_list)

t_list

pd.DataFrame(t_list)

pd.DataFrame(spider._list)
