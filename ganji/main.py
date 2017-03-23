from page_spider import get_item_info,
                        get_link_form
from channel_url import channel_url
from multiprocessing import Pool


def get_links_from(channel):
	for i in range(101):
		get_link_form(channel, i)


if __name__ == '__main__':
	pool = Pool(processes=4)
	pool.map(get_links_from, [i['url'] for i in channel_url.find()])
	pool.close()
	pool.join()
