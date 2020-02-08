class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

def countdown(n):
    print("Counting down from", n)
    while n >= 0:
        newvalue = (yield n)
        if newvalue is not None:
            n = newvalue
        else:
            n -= 1

def generateList1(start, stop):
    for i in range(start, stop):
        yield i


if __name__ == '__main__':
    # a = Counter(3, 8)
    # for c in a:
    #     print(c)
    # a = generateList1(0, 5)
    # for i in range(0, 5):
    #     print(a.send(None))

    c = countdown(5)
    for x in c:
        print(x)
        if x == 5:
            c.send(3)

