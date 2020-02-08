import asyncio
import requests
"""
在这里我们定义了一个 request() 方法，请求了百度，返回状态码，但是这个方法里面我们没有任何 print() 语句。
随后我们定义了一个 callback() 方法，这个方法接收一个参数，是 task 对象，然后调用 print() 方法打印了 task 对象的结果。
这样我们就定义好了一个 coroutine 对象和一个回调方法，我们现在希望的效果是，当 coroutine 对象执行完毕之后，就去执行声明的 callback() 方法。
那么它们二者怎样关联起来呢？只需要调用 add_done_callback() 方法即可，我们将 callback() 方法传递给了封装好的 task 对象，
这样当 task 执行完毕之后就可以调用 callback() 方法了。"""


async def request():
    url = 'https://www.baidu.com'
    status = requests.get(url)
    return status

def callback(task):
    print('Status:', task.result())

coroutine = request()
task = asyncio.ensure_future(coroutine)
task.add_done_callback(callback)
print('Task:', task)

loop = asyncio.get_event_loop()
loop.run_until_complete(task)
print('Task:', task)

loop = asyncio.get_event_loop()
loop.run_until_complete(task)
print('Task:', task)