"""
你得到一组数字，返回所有正数的总和。
示例[1,-4,7,12]=&gt;1 + 7 + 12 = 20
注意：如果没有要求的总和，则默认值为0。
"""
#
# def zhengshu(lz):
#     res = []
#     for i in lz:
#         if i > 0:
#             res.append(i)
#     if len(res) == 0:
#         return 0
#     else:
#         return sum(res)
#
# if __name__ == '__main__':
#     lz = [1,-3, -5,9,0,-1, 7,12,-4]
#     result = zhengshu(lz)
#     print(result)

def positive_sum(nums):
    return sum([n for n in nums if n >0])
