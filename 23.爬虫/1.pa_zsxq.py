import requests

header= {
 'Host': 'api.zsxq.com',
 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12;rv:57.0) Gecko/20100101 Firefox/57.0',
 'Origin': 'https://wx.zsxq.com',
 'Cookie': 'zsxq_access_token=֦ጱtoken',
 'Connection': 'keep-alive'
 }

def parse_url(self,index):
    try:
        url_base='https://api.zsxq.com/v1.10/search/topics?count=10&scope=joined&index={}&keyword={}'
        url = url_base.format(index, self.word)
        print('>>parse url:',url)
        r=requests.get(url,headers=self.header)
        res=r.json()
        if not res['succeeded']:
            return None
        return res
    except Exception as e:
        return None