import requests
from bs4 import BeautifulSoup
import time
import pymongo


client = pymongo.MongoClient('localhost', 27017)
ganji = client['ganji']
channel_url = ganji['channel_url']
start_url = 'http://bj.ganji.com/zhaopin/'
host_url = 'http://bj.ganji.com'


def get_channel_url(url):
    time.sleep(2)
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text, 'lxml')
    links = soup.select('div.f-all-news > dl > dt > a')
    for link in links:
        item_link = host_url + link.get('href')
        channel_url.insert_one({'url': item_link})
        # print(item_link)


get_channel_url(start_url)
