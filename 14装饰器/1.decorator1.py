def my_logging(func):
    def wrapper():
        print('logging-{} is running'.format(func.__name__))
        func()
    return wrapper

@my_logging
def f2():
    print("我是func函数")

f2()