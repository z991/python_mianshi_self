# 冒泡排序
"""
它重复地走访过要排序的元素列，依次比较两个相邻的元素，如果他们的顺序（如从大到小、首字母从A到Z）错误就把他们交换过来。
走访元素的工作是重复地进行直到没有相邻元素需要交换，也就是说该元素已经排序完成。
"""
import random
# def bubble_sort(data):
#     for i in range(len(data)-1):# 外循环每一次使得有序的数增加一个
#         print('i===', i)
#         indicator = False      # 用于优化（没有交换时表示已经有序，结束循环）
#         for j in range(len(data)-1-i): # 内循环每次将无需部分中的最大值放到最后面
#             print('j===', j)
#             if data[j]>data[j+1]:
#                 data[j], data[j+1] = data[j+1], data[j]
#                 indicator = True
#         if not indicator:     # 如果没有交换说明列表已经有序,结束循环
#             break

def bubble_sort(data):
    for d in range(len(data)-1, 0, -1):
        for l in range(d):
            if data[l]>data[l+1]:
                data[l], data[l+1] = data[l+1], data[l]
    return data

data = random.sample(range(1,101),4)
# data = [1,2,3,4,5]

# print('打乱顺序===', data)
# bubble_sort(data)
# print('冒泡后的排序===', data)

# 选择排序
"""
每次从待排序的数据中选取最小（最大）的一个元素，存放到序列的起始位置，直到全部排完
"""
def selectsort(data):
    for i in range(len(data)-1, 0, -1):
        maxone = 0
        for j in range(1, i+1):
            if data[j] > data[maxone]:
                maxone = j
        data[i], data[maxone] = data[maxone], data[i]
    return data
# print('打乱顺序===', data)
# selectsort(data)
# print('冒泡后的排序===', data)

# 插入排序



# 快速排序
"""
1、取一个参考值放到列表中间，初次排序后，让左侧的值都比他小，右侧的值，都比他大。

2、分别对左侧和右侧的部分递归第1步的操作
"""


def quick_sort(alist, start, end):
    if start >= end:
        # 退出递归
        return
    pivot = alist[start]
    right = end
    left = start

    # 控制right -= 1不满足条件交换
    while left < right:
        while left < right and alist[right] > pivot:
            right -= 1
        else:
            # 交换
            alist[left] = alist[right]
        # 控制 left += 1 , 不满足条件交换
        while left < right and alist[left] < pivot:
            left += 1
        else:
            alist[right] = alist[left]

    # 退出循环 left = right
    # left 或者 right 对应的位置 赋值为基准值
    alist[left] = pivot

    # 递归自己调用自己
    quick_sort(alist, start, left - 1)  # 对左边排序
    quick_sort(alist, left + 1, end)  # 对右边排序


# if __name__ == '__main__':
#     li = [6, 7, 5, 3, 4, 1, 8]
#     quick_sort(li, 0, len(li) - 1)
#     print(li)
def fib(index):
    if index <= 2:
        return 1
    else:
        return fib(index-1) + fib(index-2)

d={'lilee':25, 'wangyan':21, 'liqun':21,'lidming':19}
# sd = sorted(d.keys())
# sd = sorted(d.items(), key=lambda item:item[1])
# print(sd)
x = [{'age': 10, 'name': 'Bart'}, {'age': 39, 'name': 'Homer'}]
sx = sorted(x, key=lambda x:x['name'],reverse=True)
print(sx)
"""
类方法，实例方法，静态方法
"""

if __name__ == '__main__':
    pass
    # f100 = fib(20)
    # print(f100)