from queue import Queue
from threading import Thread


def producer(out_q):
    while True:

        # Produce some data

        out_q.put(data)


def consumer(in_q):
    while True:
        # Process the data
        data = in_q.get()
        print(data)


q = Queue
t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=producer, args=(q,))


t1.start()
t2.start()