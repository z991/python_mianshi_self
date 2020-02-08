"""
编写一个算法，该算法采用数组并将所有零移动到最后，保留其他元素的顺序。
例如
"""

# def move_zeros(l):
#     for i in l:
#         if i == 0 and len(str(i))>5:
#             l.remove(0)
#             l.append(0)
#     return l

def move_zeros1(chars):
    head = []
    tail = []
    for n in chars:
        if n == 0 and len(str(n))<5:
            tail.append(n)
        else:
            head.append(n)
    head.extend(tail)
    return head


def move_zeros(array):
    return sorted(array, key=lambda x: x ==0 and type(x) is not bool)


def move_zeros2(array):
    l = [i for i in array if isinstance(i, bool) or i !=0]
    return l+[0]*(len(array)-len(l))

def move_zeros3(array):
    return sorted(array, key=lambda x: x == 0 and x is not False)


if __name__ == '__main__':
    l = [False,1,0,0,0, 1,2,0,1,3,"a"]
    result = move_zeros3(l)
    print(result)