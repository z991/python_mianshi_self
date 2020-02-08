import asyncio
import queue
from threading import Thread

import aiohttp
import requests
from pyquery import PyQuery as pq
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Cookie": "DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; OUTFOX_SEARCH_USER_ID=-1937493410@59.111.179.141; JSESSIONID=abc6yzyqidxyw5_UUWsNw; OUTFOX_SEARCH_USER_ID_NCOO=132233581.37317117; _ntes_nnid=41ad8382575af199caa1849623d05a28,1554019212528; search-popup-show=3-31; ___rl__test__cookies=1554019301974",
    "Host": "dict.youdao.com",
    "Referer": "http://dict.youdao.com/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"}

def download_html(word):
    url = 'http://dict.youdao.com/w/eng/{}/'.format(word)
    result = {"word": word}
    try:
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            doc = pq(r.text)
            decode_dict = decode_html(doc)
            result.update(decode_dict)
    except Exception as e:
        return {"error": e}
    return result


async def async_download_html(word):
    result = {"word": word}
    session = aiohttp.ClientSession()
    url = 'http://dict.youdao.com/w/eng/{}/'.format(word)
    response = await session.get(url)
    response_text = await response.text()
    doc = pq(response_text)
    decode_dict = decode_html(doc)
    result.update(decode_dict)
    await session.close()
    return result


def cost_time(func):
    def warp(*args):
        t1 = time.time()
        func(*args)
        t2 = time.time() - t1
        print("花费了{}秒".format(t2))
    return warp


def decode_html(doc):
    proc_list = [pro.text() for pro in doc.items('.baav .pronounce .phonetic')]
    desc_list = [li.text() for li in doc.items('#phrsListTab .trans-container ul li')]

    return {"proc_list": proc_list, "desc_list": desc_list}


def async_task_by_threadingPoolExecutor(func, *args):
    pool = ThreadPoolExecutor(3)
    threads = [pool.submit(func, word) for word in args]
    for t in threads:
        print(t.result()) if t.result() else None


def async_task_by_ProcessPoolExecutor(fun, *args):
    pool = ProcessPoolExecutor(3)

    processes = [pool.submit(fun, word) for word in args]
    outputs = []
    for p in processes:
        print(p.result()) if p.result() else None




if __name__ == '__main__':
    args = ['tornado', 'pig', 'dog', 'flower', 'home', 'book', 'money', 'water','tornado', 'pig', 'dog', 'flower', 'home', 'book', 'money', 'water']
    t1 = time.time()
    async_task_by_threadingPoolExecutor(download_html, *args)
    # async_task_by_ProcessPoolExecutor(download_html, *args)
    t2 = time.time()
    print("多线程花费了{}秒".format(str(t2-t1)))
    tasks = [asyncio.ensure_future(async_download_html(word)) for word in args]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    t3 = time.time()
    print("协程花费了{}秒".format(str(t3 - t2)))