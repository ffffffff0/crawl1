import requests
from bs4 import BeautifulSoup
import time

start_url = 'http://bj.ganji.com/zhaopin/'
host_url = 'http://bj.ganji.com'


def get_channel_url(url):
    time.sleep(2)
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text, 'lxml')
    links = soup.select('div.f-all-news > dl > dt > a')
    for link in links:
        item_link = host_url + link.get('href')
        print(item_link)


get_channel_url(start_url)
channel_list = '''
http://bj.ganji.com/zpshichangyingxiao/
http://bj.ganji.com/zpjigongyibangongren/
http://bj.ganji.com/zpxingzhenghouqin/
http://bj.ganji.com/zprenliziyuan/
http://bj.ganji.com/zpjiudiancanyin/
http://bj.ganji.com/zpkefu/
http://bj.ganji.com/zptaobao/
http://bj.ganji.com/zpbaihuolingshou/
http://bj.ganji.com/zpjiazhenganbao/
http://bj.ganji.com/zpsiji/
http://bj.ganji.com/zpcaiwushenji/
http://bj.ganji.com/zpfangjingjiren/
http://bj.ganji.com/zpmeirongmeifazhiwei/
http://bj.ganji.com/zpbaojiananmo/
http://bj.ganji.com/zpyundongjianshenzhiwei/
http://bj.ganji.com/zpqiche/
http://bj.ganji.com/zpjisuanjiwangluo/
http://bj.ganji.com/zpshichanggongguan/
http://bj.ganji.com/zpguanggaohuizhanzhiwei/
http://bj.ganji.com/zpmeishusheji/
http://bj.ganji.com/zpmeitiyingshi/
http://bj.ganji.com/zplvyouzhiwei/
http://bj.ganji.com/zpjinrongtouzizhengquan/
http://bj.ganji.com/zpbaoxianjingjiren/
http://bj.ganji.com/zpzixunguwen/
http://bj.ganji.com/zpfanyi/
http://bj.ganji.com/zpjiaoyupeixun/
http://bj.ganji.com/zpbianjichuban/
http://bj.ganji.com/zpfalv/
http://bj.ganji.com/zpmaoyiyunshu/
http://bj.ganji.com/zpshengchanzhizaozhiwei/
http://bj.ganji.com/zpdianqinengyuan/
http://bj.ganji.com/zpwuye/
http://bj.ganji.com/zpjianzhuzhuangxiu/
http://bj.ganji.com/zpjixieyiqiyibiao/
http://bj.ganji.com/zpyiyaoshengwu/
http://bj.ganji.com/zpyiyuanyiliao/
http://bj.ganji.com/zpnonglin/
http://bj.ganji.com/zphuanjingbaohu/
http://bj.ganji.com/zpruanjianhulianwang/
http://bj.ganji.com/zpityunweiyuceshi/
http://bj.ganji.com/zphulianwangchanpinyunyingguanli/
http://bj.ganji.com/zpdianzidianqibandaoti/
http://bj.ganji.com/zpxintuodanbaopaimaidiandang/
http://bj.ganji.com/zpfuzhuangfangzhipigeshengchan/
http://bj.ganji.com/zphuagong/
http://bj.ganji.com/zpgaojiguanli/
http://bj.ganji.com/zpqita/
'''
