import time
import random
import asyncio
import aiohttp
from concurrent.futures import FIRST_COMPLETED
URL = 'https://baidu.com'
MAX_CLIENTS = 3
async def aiohttp_get(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return response
async def fetch_async(pid):
    start = time.time()
    sleepy_time = random.randint(2, 5)
    print('fetch coroutine {} started, sleeping for {} seconds'.format(
        pid, sleepy_time))
    response = await aiohttp_get(URL)
    datetime = response.headers.get('Date')
    #  这里增加的asyncio.sleep是为了模拟每个请求有一定延迟返回
    await asyncio.sleep(sleepy_time)
    response.close()
    return 'coroutine {}: {}, took: {:.2f} seconds'.format(
        pid, datetime, time.time() - start)
async def main():
    start = time.time()
    futures = [fetch_async(i) for i in range(1, MAX_CLIENTS + 1)]
    done, pending = await asyncio.wait(
        futures, return_when=FIRST_COMPLETED
    )
    print(done.pop().result())
asyncio.run(main())