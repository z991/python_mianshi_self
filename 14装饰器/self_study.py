import time


# def add(x, y):
#     t1 = time.time()
#     time.sleep(1)
#     result = x + y
#     t2 = time.time()
#     return result
#
#
def timmer(func):
    def f1(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print("时间花费了{}秒".format(str(t2 - t1)))
        return result

    return f1
#
#
@timmer
def jain(x, y):
    result = x - y
    return result
#
#
# def timer(func, x, y):
#     t1 = time.time()
#     result = func(x, y)
#     t2 = time.time()
#     print("时间花费了{}秒".format(str(t2 - t1)))
#     return result




if __name__ == '__main__':
    res = jain(8, 10)
    print(res)
