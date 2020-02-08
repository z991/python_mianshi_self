import time

def countdown(n):
    while n > 0:
        print('T-MINUS', n)
        n -= 1
        time.sleep(5)

from threading import Thread
# t = Thread(target=countdown, args=(5,))
#
#
# t.start()
# if t.is_alive():
#     print('Still running')
# else:
#     print('Completed')

class CountdownTask:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, n):
        while self._running and n > 0:
            print('T-minus', n)
            n -= 1
            time.sleep(5)


# c = CountdownTask()
# t = Thread(target=c.run, args=(10,))
# t.start()
# # c.terminate() #终止线程
# t.join() # 等待实际终止（如果需要）

class CountdownThread(Thread):
    def __init__(self, n):
        super().__init__()
        self.n = n

    def run(self):
        while self.n > 0:
            print('T-minus', self.n)
            self.n -= 1
            time.sleep(5)

# c = CountdownThread(5)
# c.start()
import multiprocessing
c = CountdownTask()
p = multiprocessing.Process(target=c.run, args=(5,))
p.start()
