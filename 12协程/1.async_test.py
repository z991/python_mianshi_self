import asyncio
from asyncio import AbstractEventLoop

import aiohttp
import requests
import bs4
from colorama import Fore
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def main():
    # Create loop
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_title_range(loop))
    print("Done.")


async def get_html(episode_number: int) -> str:
    print(Fore.YELLOW + f"Getting HTML for episode {episode_number}", flush=True)
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

    # Make this async with aiohttp's ClientSession
    url = f'http://www.baidu.com/s?wd={episode_number}&rsv_spt={episode_number}'
    # resp = await requests.get(url)
    # resp.raise_for_status()

    async with aiohttp.ClientSession() as session:
        async with session.get(url, ssl=sslcontext) as resp:
            resp.raise_for_status()

            html = await resp.text()
            print("html=======", html)
            return html


def get_title(html: str, episode_number: int) -> str:
    print(Fore.CYAN + f"Getting TITLE for episode {episode_number}", flush=True)
    soup = bs4.BeautifulSoup(html, 'html.parser')
    header = soup.select_one('h1')
    if not header:
        return "MISSING"

    return header.text.strip()


async def get_title_range(loop: AbstractEventLoop):
    # Please keep this range pretty small to not DDoS my site. ;)
    tasks = []
    for n in range(190, 200):
        tasks.append((loop.create_task(get_html(n)), n))

    for task, n in tasks:
        html = await task
        title = get_title(html, n)
        print(Fore.WHITE + f"Title found: {title}", flush=True)


if __name__ == '__main__':
    main()