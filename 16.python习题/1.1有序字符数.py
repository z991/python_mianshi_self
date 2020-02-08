"""
例如给你一个字符串"abracadabra"，统计里面的字符按照下面的格式输出:
ordered_count("abracadabra") == [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]
"""

from collections import Counter


class OrderedCounter(Counter):
    pass


def ordered_count(seq):
    return list(OrderedCounter(seq).items())

if __name__ == '__main__':
    seq = "abracadabra"
    result = ordered_count(seq)
    print(result)