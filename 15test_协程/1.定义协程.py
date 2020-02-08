import asyncio
"""
async定义的方法会变成一个无法执行的coroutine对象,
必须注册到时间循环中才可以执行
"""

async def execute(x):
    print('Number:', x)

# 调用execute方法，返回一个coroutine协程对象
coroutine = execute(1)
print('Coroutine:', coroutine)
print('After calling execute')
# 创建一个事件循环
loop = asyncio.get_event_loop()
# 将协程注册到事件循环loop中，然后启动
loop.run_until_complete(coroutine)
print('After calling loop')