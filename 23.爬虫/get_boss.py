import requests
import json

headers = {"authority": "www.zhipin.com",
"method": "GET",
"path": "/c101010100/?query=python&period=1&ka=sel-scale-1",
"scheme": "https",
"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/,apng,*/*;q=0.8,application/'signed-exchange;v=b3",
"accept-encoding": "gzip, deflate, br",
"accept-language": "zh-CN,zh;q=0.9",
"cache-control": "max-age=0",
"cookie": "lastCity=101010100; _uab_collina=155706567566450357631973; __c=1557922865; __g=-; __l=l=%2Fwww.zhipin.com%2F&r=; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1557065676,1557922865; t=LPKiw0eVhhqRzyhh; wt=LPKiw0eVhhqRzyhh; JSESSIONID=C61PlSNBSwuqqD7UuZVrhskWmAIdQT6XiM89c2_k; __a=44096022.1557065676.1557065676.1557922865.29.2.19.29; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1557928822",
"upgrade-insecure-requests": "1",
"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"}


response = requests.get(url="https://www.zhipin.com/c101010100/?query=python&period=1&ka=sel-scale-1",
                        headers=headers)
content = response.content
bod = str(content, encoding="utf-8")
print(bod)