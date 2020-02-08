import random

def apple_key(l, n):
    """
    :param l: 激活码长度
    :param n: 激活码个数
    :return:
    """
    str = "1234567890ASDFGHJKLQWERTYUIOPZXCVBNM"
    key_set = set()

    while len(key_set) <n:
        res = ''.join(random.sample(str, l))
        key_set.add(res)
    return key_set

if __name__ == '__main__':
    result = apple_key(12, 200)
    print(result)
