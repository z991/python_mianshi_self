import asyncio
from socket import socketpair

# Create a pair of connected file descriptors
rsock, wsock = socketpair()
loop = asyncio.get_event_loop()

def reader():
    data = rsock.recv(100)
    print("Received:", data.decode())
    # We are done: unregister the file descriptor
    loop.remove_reader(rsock)
    # Stop the event loop
    loop.stop()

loop.add_reader(rsock, reader)
loop.call_soon(wsock.send, 'abc'.encode())

loop.run_forever()

rsock.close()
wsock.close()
loop.close()