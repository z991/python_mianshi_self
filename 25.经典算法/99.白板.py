def quick_sort(alist, first, last):
    if first > last:
        return
    mid_value = alist[first]
    low = first
    high = last

    while low < high:
        if low < high and alist[high] >= mid_value:
            high = high - 1
        alist[low] = alist[high]
        if low < high and alist[low] < mid_value:
            low = low + 1
        alist[high] = alist[low]
    alist[low] = mid_value
    quick_sort(alist, first, low - 1)
    quick_sort(alist, low + 1, last)
    return alist


import random


def simple_quick(numberts):
    if len(numberts) <= 1:
        return numberts

    left, right, mid = [], [], []
    pivot = random.choice(numberts)
    for number in numberts:
        if number == pivot:
            mid.append(number)
        elif number < pivot:
            left.append(number)
        else:
            right.append(number)
    return simple_quick(left) + mid + simple_quick(right)


def binary_search(arr, start, end, hkey):
    if start > end:
        return -1
    mid = start + (end - start) / 2
    if arr[mid] < hkey:
        binary_search(arr, mid+1, end, hkey)
    if arr[mid] > hkey:
        binary_search(arr, start, mid-1, hkey)
    return mid


if __name__ == '__main__':
    array = [2, 3, 5, 7, 1, 4, 15, 5, 2, 7, 9, 10, 15, 9, 17, 12]
    # array = [6, 2, 9, 7, 17, 3, 5, 12]
    # print(quick_sort(array))
    print(quick_sort(array, 0, len(array) - 1))
