import asyncio
import functools
import os
import signal

loop = asyncio.get_event_loop()

def ask_exit(signame):
    print("got signal %s:exit" % signame)
    loop.stop()

for signame in ('SIGNT', 'SIGTERM'):
    loop.add_signal_handler(getattr(signal, signame),
                            functools.partial(ask_exit, signame))

print("Event loop running forever, press Ctrl+C to interrupt.")
print("pid %s: send SIGINT or SIGTERM to exit." % os.getpid())

try:
    loop.run_forever()
finally:
    loop.close()