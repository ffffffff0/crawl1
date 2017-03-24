# final

![py35](https://camo.githubusercontent.com/633acad03f4dbbaa8cca6bee5902207fd3b27a34/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2d332e352d7265642e737667)

这是一个赶集网的爬虫，主要爬取赶集网上的招聘的板块上的信息。

## 依赖

- MongoDB
- requests
- pymongo
- BeautifulSoup and lxml

## 关于爬虫

### 准备

1. 确定已安装MongoDB，Python3.5, 浏览器建议使用Chrome。
2. 安装需要的Python的第三方库:

	```
	在 terminal(cmd) 中输入：

	win:

	pip install requests, BeautifulSoup4, pymongo, lxml

	linux:

	sudo pip3 install requests, BeautifulSoup4, pymongo, lxml

	```

3. 如果你知道更好：
	- 一点 HTML CSS HTTP and MongoDB

### 整体结构
![stru](test.jpg)

spider 1 从[列表页](http://bj.ganji.com/zhaopin/)中获取页面下全部的个分类的链接，并储存到 url_list 这个collection中。

Spider 2 从url_list 中获取储存的链接并解析，这里我每个分类只抓取了100页，获取链接的详情页，将详情页中的想要抓取的信息储存到 item_info 中。

###
