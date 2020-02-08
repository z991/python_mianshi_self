import time, threading
blance = 1000
lock = threading.Lock()


def chande_it(n):
    global balance
    balance = balance+n
    balance = balance-n


def run_thread(n):
    for i in range(100000):
        lock.acquire()
        try:
            chande_it(n)
        finally:
            lock.release()

def main():
    print(time.ctime())
    t1 = threading.Thread(target=run_thread, args=(1,))
    t2 = threading.Thread(target=run_thread, args=(10,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(time.ctime())

if __name__ == '__main__':
    main()
    print(balance)