"""
每秒显示当前日期的回调示例。回调使用该AbstractEventLoop.call_later()方法在5秒内重新安排自己，然后停止事件循环：
"""
import asyncio
import datetime

def display_date(end_time, loop):
    print(datetime.datetime.now())
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, display_date, end_time, loop)
    else:
        loop.stop()

loop = asyncio.get_event_loop()

end_time = loop.time() + 9.0
loop.call_soon(display_date, end_time, loop)

loop.run_forever()
loop.close()