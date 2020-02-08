"""
编写一个函数，该函数将返回在输入字符串中出现多次(不同的不区分大小写的)字母字符和数字的计数。
可以假定输入字符串仅包含字母（大写和小写）和数字。
"""
from collections import Counter

def tongji_word(string):
    string = string.lower()
    res = [each for each in Counter(string).most_common() if each[1]>1]
    return len(res)

def duplicate_cout(s):
    return len([c for c in set(s.lower()) if s.lower().count(c)>1])

def duplicate_count(text):
    return sum(1 for c, n in Counter(text.lower()).items() if n >1)

def practise_count(string):
    res = Counter(string.lower())
    print(res)
    return res


if __name__ == '__main__':
    string = "aaByyyyy5678haabbcde"
    result = tongji_word(string)
    most = Counter(string).most_common()
    print(most)
    print(result)