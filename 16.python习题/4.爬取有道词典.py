# from pyquery import PyQuery as pq
# import aiohttp
# import asyncio
# import time

# def decode_html(html_content):
#     doc = pq(html_content)
#     des = ''
#     for li in doc.items('#phrsListTab.trans-container ul li'):
#         des += li.text()
#     return des


# async def fetch(session, url):
#     async with session.get(url) as response:
#         return await response.text()


# async def main(words):
#     urls = ['http://dict.youdao.com/w/eng/{}'.format(word) for word in words]
#     tasks = []
#     async with aiohttp.ClientSession() as session:
#         for url in urls:
#             tasks.append(fetch(session, url))
#         htmls = await asyncio.gather(*tasks)
#         for html_content in htmls:
#             print(decode_html(html_content))

# async def main(words):
#     tasks = []
#     async with aiohttp.ClientSession() as session:
#         for word in words:
#             tasks.append(fetch(session, word))
#         res_list = await asyncio.gather(*tasks)
#         for index,each in enumerate(res_list):
#             print(index+1, each['word'], '->', await(decode_html()))

# if __name__ == '__main__':
#     s = time.time()
#     text = "apple"
#     words = text.split()
#     words = words*100
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main(words=words))
#     print(time.time()-s)

import aiohttp
import asyncio
import time

from pyquery import PyQuery as pq

async def decode_html(html_content):
    """
    接卸网页
    :param html_content:
    :return:
    """
    doc=pq(html_content)
    des=''
    for li in doc.items("#phrsListTab .trans-container ul li"):
        des+=li.text()
    return des

async def fetch(session, word):
    """
    发起get请求
    :param session:
    :param word:
    :return:
    """
    url='http://dict.youdao.com/w/eng/{}'.format(word)
    async with session.get(url) as response:
        return {'word':word,'data':await response.text()}

async def main(words):
    tasks = []
    async with aiohttp.ClientSession() as session:
        for word in words:
            tasks.append(fetch(session, word))
        res_list = await asyncio.gather(*tasks)
        for index,each in enumerate(res_list):
            print(index+1,each['word'],'-&gt;',await(decode_html(each['data'])))

if __name__ == '__main__':
    s=time.time()
    text="apple bannal"
    words=text.split()
    words=words*100
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(words=words))
    print(time.time()-s)