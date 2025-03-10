import asyncio

async def execute(x):
    print('Number:', x)
    return x

coroutine = execute(1)
print('Coroutine:', coroutine)
print('After calling execute')
"""
定义 task 对象还有一种方式，就是直接通过 asyncio 的 ensure_future() 方法，
返回结果也是 task 对象，这样的话我们就可以不借助于 loop 来定义，
即使我们还没有声明 loop 也可以提前定义好 task 对象
"""
task = asyncio.ensure_future(coroutine)
print('Task:', task)
loop = asyncio.get_event_loop()
loop.run_until_complete(task)
print('Task:', task)
print('After calling loop')