import asyncio
import time

"""
生成一个多任务的相加的函数，简便操作我们用zip构造10组x,y参数
然后把这个10个add函数，也就是10个协程放到一个tasks列表里面
最后塞到事件循环里面，等待它们完成
"""

async def add(x=1, y=2):
    print("Add {}+{}..".format(x, y))
    await asyncio.sleep(2)
    return x + y

s = time.time()
loop = asyncio.get_event_loop()
tasks = [add(x, y) for x, y in zip(range(1,10), range(11,20))]
loop.run_until_complete(asyncio.wait(tasks))
print('cost:', time.time()-s)