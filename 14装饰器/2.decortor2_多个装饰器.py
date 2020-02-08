import time

def timeer(func):
    def wrapper():
        time_start = time.time()
        func()
        time.sleep(2)
        print('Cost:{}秒'.format(time.time() -time_start))
        return func()
    return wrapper

def bold(func):
    def wrapper():
        print("<b>")
        func()
        print("</b>")
        return func()
    return wrapper


def italic(func):
    def wrapper():
        print("<i>")
        func()
        print("</i>")
        return func()

    return wrapper


@timeer
@bold
@italic
def cheng():
    b=8*5
    return b

print(cheng())
