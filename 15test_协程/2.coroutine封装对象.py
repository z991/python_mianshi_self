import asyncio

async def execute(x):
    print('Number:', x)
    return x

coroutine = execute(1)
print('Coroutine:', coroutine)
print('After calling execute')

loop = asyncio.get_event_loop()
# 将coroutinge对象转化为task对象
task = loop.create_task(coroutine)
print('Task:' ,task)
loop.run_until_complete(task)
print('Task', task)
print('After calling loop')