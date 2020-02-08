import random


# def quick_sort(numbers):
#     """python 简单快速排序"""
#     if len(numbers) <= 1:
#         return numbers
#
#     left, right, mid = [], [], []
#     pivot = random.choice(numbers)
#
#     for number in numbers:
#         if number == pivot:
#             mid.append(number)
#         elif number < pivot:
#             left.append(number)
#         else:
#             right.append(number)
#
#     return quick_sort(left) + mid + quick_sort(right)
# def situ_quick_sort(alist, first, last):
#     """
#     快速排序  原地排序
#     https://cloud.tencent.com/developer/article/1012163
#
#     :param alist:
#     :param first:
#     :param last:
#     :return:
#     """
#     if first >= last:
#         return
#
#     mid_value = alist[first]
#     low = first
#     high = last
#
#     while low < high:
#         while low < high and alist[high] >= mid_value:  # 从右侧开始扫描
#             high -= 1
#         alist[low] = alist[high]
#         while low < high and alist[low] < mid_value:  # 从左侧开始扫描
#             low += 1
#         alist[high] = alist[low]
#     alist[low] = mid_value
#     situ_quick_sort(alist, first, low-1)
#     situ_quick_sort(alist, low+1, last)
#     return alist


def situ_quick_sort(alist, first, last):
    """
    快速排序
    :param alist:
    :param first:
    :param last:
    :return:
    """
    if first >= last:
        return

    mid_value = alist[first]
    low = first
    high = last

    while low < high:
        while low < high and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]
        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]
    alist[low] = mid_value
    situ_quick_sort(alist, first, low - 1)
    situ_quick_sort(alist, low+1, last)
    return alist




if __name__ == "__main__":
    array = [2, 3, 5, 7, 1, 4, 15, 5, 2, 7, 9, 10, 15, 9, 17, 12]
    # array = [6, 2, 9, 7, 17, 3, 5, 12]
    # print(quick_sort(array))
    print(situ_quick_sort(array, 0, len(array)-1))
