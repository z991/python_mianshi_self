import asyncio
import time


def hell_world(loop):
    print('Hello World')
    loop.stop()

loop = asyncio.get_event_loop()
# Schedule a call to hello_world()
loop.call_soon(hell_world, loop)
# Blocking call interrupted by loop.stop()
loop.run_forever()
loop.close()
