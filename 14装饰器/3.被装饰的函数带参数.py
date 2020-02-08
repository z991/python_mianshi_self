import time

def my_logging(func):
    def wrapper(*args, **kwargs):
        print('logging - {} is running'.format(func.__name__))
        func(*args, **kwargs)
    return wrapper

def timeer(func):
    def wrapper(*args, **kwargs):
        time_start = time.time()
        res = func(*args, **kwargs)
        time.sleep(2)
        print(args, '========')
        print('Cost:{}秒'.format(time.time() -time_start))
        print(res, 'func=====')
        return res
    return wrapper

@timeer
def f1(*args, **kwargs):
    b = 9*20*34
    for thing in args:
        print('hello {}'.format(thing))
    for name, value in kwargs.items():
        print('{0}={1}'.format(name, value))
    return b

f1('twtrubiks', appel='fruit', cabbage='begetable')