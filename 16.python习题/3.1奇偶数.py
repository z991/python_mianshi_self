# def jou_num(num):
#     try:
#         assert isinstance(num, int)
#     except AssertionError:
#         return '类型必须为整数类型'
#     if num % 2 == 0:
#         return '偶数'
#     else:
#         return '奇数'

# def jou_num(num):
#     return ["偶数", "奇数"][num % 2]

# def jou_num(num):
#     return '偶数' if num % 2 == 0 else '奇数'
#
# if __name__ == '__main__':
#     r = jou_num(1)
#     print(r)