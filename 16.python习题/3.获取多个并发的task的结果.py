import asyncio
import time


async def add(x=1, y=2):
    print("Add {}+{}..".format(x, y))
    await asyncio.sleep(2)
    return x + y

s = time.time()
loop = asyncio.get_event_loop()
tasks = [loop.create_task(add(x, y)) for x, y in zip(range(1,10), range(11,20))]
loop.run_until_complete(asyncio.wait(tasks))

"""
如果我们要获取task的结果，一定要创建一个task, 就是把我们的协程绑定要task上,这里直接用事件循环loop里面的create_task就可以搞定。
我们假设有3个并发的add任务需要处理,然后调用run_until_complete来等待3个并发任务完成。
调用task.result查看结果，这里的task其实是_asyncio.Task,是封装的一个类。
大家可以在Pycharm中找asyncio里面的源码，里面有一个tasks文件.
"""

# tasks = [loop.create_task(add(1, 2)),
#          loop.create_task(add(11, 12)),
#          loop.create_task(add(111, 112))]
# loop.run_until_complete(asyncio.wait(tasks))
for task in tasks:
    print(task.result())

print('cost:', time.time()-s)