import requests
from bs4 import BeautifulSoup
import pymongo
import re
import random
import time

# 连接mongodb
client = pymongo.MongoClient('localhost', 27017, connect=False)
ganji = client['ganji']
item_info = ganji['item_info']
url_list = ganji['url_list2']

# 设置头部
header = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Ubuntu/11.10 Chromium/27.0.1453.93 Chrome/27.0.1453.93 Safari/537.36',
    'Connection': 'keep-alive'
}

# 设置代理
proxy_list = [
    # 'http://111.7.174.132:8000',
    # 'http://125.88.74.122:82',
    # 'http://125.88.74.122:84',
    # 'http://125.88.74.122:83',
    # 'http://111.7.175.33:8080',
    # 'http://111.7.175.27:80'
]
# 使用random 随机使用一个代理ip
proxy_ip = random.choice(proxy_list)
proxies = {'http': proxy_ip}
# spider 1


def get_link_form(channel, page):
    url_views = '{0}o{1}/'.format(channel, str(page))
	# 程序暂停1s
	time.sleep(1)
    web_data = requests.get(url_views, headers=header, proxies=proxies)
    soup = BeautifulSoup(web_data.text, 'lxml')
	# 判断是否是有效的页面
    if soup.find('ul', 'pageLink'):
		# 利用正则匹配到 url
        links = soup.findAll('a', href=re.compile('^(https?://)?bj\.ganji\.com.*\.htm'))
        for link in links:
            url_list.insert_one({'url': link.get('href')})
            print(link.get('href'))
    else:
        pass

# spider 2


def get_item_info(url):
    wd_data = requests.get(url, headers=header)
	# 判断页面的是否有效
    if wd_data.status_code == 404:
        pass
    else:
        soup = BeautifulSoup(wd_data.text, 'lxml')
        # select return list, find return   <class 'bs4.element.Tag'>
		# 将所需要的信息装进一个字典中
        data = {
            'title': soup.select('div.d-c-left-hear > h1')[0].text,
            'postion_name': soup.select('div.d-c-left-age.d-c-left-firm.mt-30 > ul > li:nth-of-type(1) > em > a')[0].text,
            'Education': soup.select('div.d-c-left-age.d-c-left-firm.mt-30 > ul > li:nth-of-type(3) > em')[0].text,
            'salary': soup.find('em', {'class': 'salary'}).get_text(),
            'work_experience': soup.select('div.d-c-left-age.d-c-left-firm.mt-30 > ul > li:nth-of-type(4) > em')[0].text,
            'want_person': soup.select('div.d-c-left-age.d-c-left-firm.mt-30 > ul > li:nth-of-type(6) > em')[0].text,
            'adress': list(soup.select('div.d-c-left-age.d-c-left-firm.mt-30 > ul > li:nth-of-type(8) > em')[0].stripped_strings),
            'wants': soup.find('span', {'class': 'delivery-num'}).get_text().split('：')[1],
            'age': soup.select(' div.d-c-left-age.d-c-left-firm.mt-30 > ul > li:nth-of-type(5) > em')[0].text,
            'welfare': list(soup.select('div.d-c-left-weal.d-left-weal-firm.clearfix.mb-30 > div > ul')[0].stripped_strings),
        }
        item_info.insert_one(data)
        print(data)
