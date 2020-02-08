import aiohttp
import asyncio
import time
import os
import ssl


from pyquery import PyQuery as pq
COUNT = 1

async def parse_url(doc):
    info = {}
    info['Desc'] = ''
    doc = pq(doc)
    items = list(doc.items('.mw-parser-output .hatnote'))
    if len(items) > 1:
        info['Desc'] = items[0].text()
    return info

async def fetch(session, *args):
    FORCED_CIPHERS = (
        'ECDH+AESGCM:DH+AESGCM:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+HIGH:'
        'DH+HIGH:ECDH+3DES:DH+3DES:RSA+AESGCM:RSA+AES:RSA+HIGH:RSA+3DES'
    )
    sslcontext = ssl.create_default_context()
    sslcontext.options |= ssl.OP_NO_SSLv3
    sslcontext.options |= ssl.OP_NO_SSLv2
    sslcontext.options |= ssl.OP_NO_TLSv1_1
    sslcontext.options |= ssl.OP_NO_TLSv1_2
    sslcontext.set_ciphers(FORCED_CIPHERS)
    url_base, word = args
    url = '{}/{}'.format(url_base, word)
    async with session.get(url, ssl=sslcontext) as response:
        return {'word': word, 'data': await response.text()}

async def main(url_base, words):
    tasks = []
    async with aiohttp.ClientSession() as session:
        for word in words:
            tasks.append(fetch(session, url_base, word))
        res_list = await asyncio.gather(*tasks)
        for index, each in enumerate(res_list):
            print(index + 1, each['word'], '-&gt;', await(parse_url(each['data'])))

if __name__ == '__main__':
    words = ['China', 'America', 'England', 'France', 'Germany']
    url_base = 'https://en.wikipedia.org/wiki'
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(url_base, words))