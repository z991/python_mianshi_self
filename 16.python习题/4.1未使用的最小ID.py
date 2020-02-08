from functools import reduce
# def next_id(array):
#     if not array:
#         return 0
#
#     sorted_arr = set(sorted(array))
#     array = set(range(0, max(array)+1))
#     gap = array - sorted_arr
#     if gap:
#         return min(gap)
#     else:
#         return 0 if 0 not in sorted_arr else max(sorted_arr)+1

def next_id(arr):
    t = 0
    while t in arr:
        t += 1
    return t

# def next_id(arr):
#     return reduce(lambda acc, x: acc + 1 if x == acc else acc, sorted(arr), 0)
#
#
# if __name__ == '__main__':
#     array = [5,4,3,2,0]
#     result = next_id(array)
#     print(result)

# list = [1,2,3,4,5,6]
# def jia(x,y):
#     return x+y
#
# # res = lambda x:reduce(jia, list)
# res = reduce(jia, list)
if __name__ == '__main__':
    ls = [0,0,0,0,0,0]
    res = next_id(ls)
    print(res)
