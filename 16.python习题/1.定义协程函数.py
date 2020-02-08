import asyncio
import time

"""
从Python3.5开始引入了async和await ，方便我们更好的使用asyncio这个库。
async就是声明一个函数为协程。而await就是代替原来的yield from。
协程里面是不能有阻塞操作的，对于sleep这样的阻塞我们需要用关键是await来包装一下，可以理解为执行一个sleep的协程，sleep 2秒
协程需要搭配事件循环才能使用,用asyncio库里面的get_event_loop来声明一个异步的事件循环
然后把我们的add函数注册到loop中去
最后我们等待事件完成run_until_complete
"""

async def add(x=1, y=2):
    print("Add {}+{}..".format(x, y))
    await asyncio.sleep(2)
    return x + y

s = time.time()
loop = asyncio.get_event_loop()
loop.run_until_complete(add())
print('cost:', time.time()-s)