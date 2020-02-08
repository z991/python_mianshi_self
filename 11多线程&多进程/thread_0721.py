import logging
import threading
import time
"""
16:12:16: Main  : before creating thread
16:12:16: Main : before running thread
16:12:16: Thread 1: starting
16:12:16: Main  :waite for the thread to finish
16:12:18: Thread 1: finshing
16:12:18: Main  : all done
"""

"""
守护进程daemon在Python线程模块threading中有着特殊的含义。当程序退出时，守护线程将立即关闭。可以这么理解，守护线程是一个在后台运行，且不用费心去关闭它的线程，因为它会随程序自动关闭。
如果程序运行的线程是非守护线程，那么程序将等待所有线程结束后再终止。但如果运行的是守护线程，当程序退出时，守护线程会被自动杀死。

"""

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finshing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    # logging.info("Main  : before creating thread")
    # # x = threading.Thread(target=thread_function, args=(1,))
    # x = threading.Thread(target=thread_function, args=(1,), daemon=True)
    # logging.info("Main : before running thread")
    # x.start()
    # logging.info("Main  :waite for the thread to finish")
    # # x.join()
    # logging.info("Main  : all done")

    threads = list()
    for index in range(3):
        logging.info("Main    : create and start thread %d.", index)
        x = threading.Thread(target=thread_function, args=(index, ))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        logging.info("Main : before joining thread %d.", index)
        thread.join()
        logging.info("Main : thread %d done", index)
