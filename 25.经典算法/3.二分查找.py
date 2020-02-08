
def binary_search(_list, num):

    mid = len(_list) // 2
    if len(_list) < 1:
        return False
    if num > _list[mid]:
        binary_search(_list[mid:], num)
    elif num < _list[mid]:
        binary_search(_list[:mid], num)
    else:
        print(_list.index(num))
        return _list.index(num)


def binary_search_w(arr, start, end, hkey):
    if start > end:
        return -1
    mid = start + (end - start) // 2
    if arr[mid] > hkey:
        return binary_search_w(arr, start, mid - 1, hkey)
    if arr[mid] < hkey:
        return binary_search_w(arr, mid + 1, end, hkey)
    return mid


def er_fen(_list, start, end, num):
    if start > end:
        return -1
    mid = start + (end - start) // 2


    if _list[mid] < num:  # 右半部分
        return er_fen(_list, mid+1, end, num)

    if _list[mid] > num:
        return er_fen(_list, start, mid-1, num)

    else:
        return mid

if __name__ == '__main__':
    _list = [1,2,4,5,6,9,7,8,9,10, 30, 50]
    n = binary_search_w(_list, 0, 11, 2)
    print(n)