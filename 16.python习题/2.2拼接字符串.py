"""
根据下面的表达式设计一个函数:
accum("abcd") -&gt; "A-Bb-Ccc-Dddd"
accum("RqaEzty") -&gt; "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -&gt; "C-Ww-Aaa-Tttt"
"""
# def accum(test_str):
#     str_list = []
#     n = 1
#     for s in test_str:
#         ss = s.upper() + s.lower()*(n-1)
#         n += 1
#         str_list.append(ss)
#     return '-'.join(str_list)
#
# if __name__ == '__main__':
#     test_str = 'cwAt'
#     result = accum(test_str)
#     print(result)

# def accum(words):
#     res = [c * (index + 1) for index, c in enumerate(words)]
#     return '-'.join(map(lambda x: x.capitalize(), res))

# def accum(s):
#     return '-'.join(c.upper()+c.lower() * i for i, c in enumerate(s))