"""
给定一个数字，写一个函数来输出其反向数字，反转时负数仍应为负数
"""


def reverseNumber(n):
    if n < 0:return -reverseNumber(-n)
    return int(str(n)[::-1])

def reverseNumbers(n):
    return int(str(abs(n))[::-1]) * (-1 if n < 0 else 1)


if __name__ == '__main__':
    result = reverseNumbers(-564534)
    print(result)
