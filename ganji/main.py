from page_spider import get_item_info, get_link_form
from multiprocessing import Pool
# from channel_url import channel_list
from page_spider import url_list


# def get_links_from(channel):
#     for i in range(1, ):
#         get_link_form(channel, i)


if __name__ == '__main__':
    pool = Pool(4)
	# 从数据库中将url迭代出来
    for link in url_list.find({}, {'_id': 0, 'url': 1}):
        pool.apply(get_item_info, args=(link['url'],))
    pool.close()
    pool.join()

# if __name__ == '__main__':
# 	pool = Pool(4)
# 	pool.map(get_links_from, channel_list.split())
