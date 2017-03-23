import requests
from bs4 import BeautifulSoup
import time
import pymongo
import re
import random


client = pymongo.MongoClient('localhost', 27017)
ganji = client['ganji']
item_info = ganji['item_info']
url_list = ganji['url_list']

# spider1

header = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Ubuntu/11.10 Chromium/27.0.1453.93 Chrome/27.0.1453.93 Safari/537.36',
	'Connection':'keep-alive'
}

proxy_list = [

]
proxy_ip = random.choice(proxy_list)
proxies = {'http': proxy_ip}
# http://bj.ganji.com/zpjigongyibangongren/o10/
# href="http://bj.ganji.com/zpjigongyibangongren/2684481590x.htm"


def get_link_form(channel, page):
    url_views = '{}o{}/'.format(channel, str(page))
    web_data = requests.get(url_views, headers=header, proxies=proxies)
    soup = BeautifulSoup(web_data.text, 'lxml')
    if soup.find('dl', 'dt'):
        links = soup.findAll('a', href=re.compile('^(https?://)?bj\.ganji\.com.*\.htm'))
        for link in links:
            url_list.insert_one({'url': link.get('href')})
    else:
        pass


# get_link_form('http://bj.ganji.com/zpjigongyibangongren/'
#spider 2


def get_item_info(url):
    wd_data = requests.get(url, headers=header)
    if wd_data.status_code == 404:
        pass
    else:
        soup = BeautifulSoup(wd_data.text, 'lxml')
        # select return list, find return   <class 'bs4.element.Tag'>
        data = {
            'title': soup.select('div.d-c-left-hear > h1')[0].text,
            'postion_name': soup.select('div.d-c-left-age.d-c-left-firm.mt-30 > ul > li:nth-of-type(1) > em > a')[0].text,
            'Education': soup.select('div.d-c-left-age.d-c-left-firm.mt-30 > ul > li:nth-of-type(3) > em')[0].text,
            'salary': soup.find('em', {'class': 'salary'}).get_text(),
            'work_experience': soup.select('div.d-c-left-age.d-c-left-firm.mt-30 > ul > li:nth-of-type(4) > em')[0].text,
            'want_person': soup.select('div.d-c-left-age.d-c-left-firm.mt-30 > ul > li:nth-of-type(6) > em')[0].text,
            'adress': soup.select('div.d-c-left-age.d-c-left-firm.mt-30 > ul > li:nth-of-type(8) > em')[0].text,
            'views': soup.find('span', {'id': 'pageviews'}).get_text(),
            'wants': soup.find('span', {'class': 'delivery-num'}).get_text().split('：')[1],
			'age': soup.select(' div.d-c-left-age.d-c-left-firm.mt-30 > ul > li:nth-of-type(5) > em')[0].text,
			'welfare': list(soup.select('div.d-c-left-weal.d-left-weal-firm.clearfix.mb-30 > div > ul')[0].stripped_strings),
        }
        item_info.insert_one(data)


# get_item_info('http://bj.ganji.com/zpshichangyingxiao/2418829460x.htm')
