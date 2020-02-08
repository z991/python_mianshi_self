list1 = [2, 3, 8, 4, 9, 5, 6]
list2 = [5, 6, 10, 17, 11, 2]
a=[1,2,3,2,3,5,7,10,5,5,5,7,8,9,0,3]


def BubbleSort(A):
    n = len(A)
    for i in range(n - 1):
        for j in range(n - 1, i, -1):
            if A[j] < A[j - 1]:
                tmp = A[j]
                A[j] = A[j - 1]
                A[j - 1] = tmp
    return A

def list_sort(l):
    n = len(l)
    for i in range(n-1):
        for j in range(n-1, i, -1):
            if l[j] < l[j-1]:
                l[j], l[j-1] = l[j-1], l[j]
    return l

li = list_sort(a)
print(li)