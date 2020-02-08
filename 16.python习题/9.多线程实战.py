from requests import ConnectTimeout
from pyquery import PyQuery as pq
from concurrent.futures import ThreadPoolExecutor
import requests

COUNT = 1


def parse_html(doc):
    proc_text = ''
    desc_text = ''

    for pro in doc.items('.baav .pronounce'):
        proc_text += pro.text()

    for li in doc.items('#phrsListTab .trans-container ul li'):
        desc_text += li.text()

    return {'Proc': proc_text, 'Desc': desc_text}


def translate_word(word):
    global COUNT
    output = {}
    url = 'http://dict.youdao.com/w/eng/{}/'.format(word)
    print('{},Fetch:{}'.format(COUNT, url))
    COUNT += 1
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

    try:
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            doc = pq(r.text)
            info = parse_html(doc)
            output['Word'] = word
            output = dict(output, **info)

    except ConnectTimeout as e:
        print('Get url:{} timeout'.format(url))
    except ConnectionError as e:
        print('Get url:{} error'.format(url))
    except Exception as e:
        print(e)

    return output

def async_task(words):
    pool = ThreadPoolExecutor(4)
    threads = [pool.submit(translate_word, (word)) for word in words]
    for t in threads:
        print(t.result())

if __name__ == '__main__':
    words = ['china', 'english', 'tmperaments']
    async_task(words)