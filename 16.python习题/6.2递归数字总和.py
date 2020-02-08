# def digital_root(num):
#     if len(str(num)) > 1:
#         arr = list(str(num))
#         s = sum(map(int, arr))
#         if len(str(s))>1:
#             digital_root(s)
#         return s

def digital_root(num):
    num_l = {"num": num}
    if len(str(num)) == 1:
        print('=>', num)
        num_l["num"] = num
    else:
        arr = list(str(num))
        print('=>', '+'.join(arr))
        s = sum(map(int, arr))
        if len(str(s)) > 1:
            print('=>', s, '...')
        digital_root(s)
    return num_l


def digital_root_dg(string):
    if len(string) > 1:
        ls = [int(s) for s in string]
        ls = sum(ls)
        ls = str(ls)
        return digital_root(ls)

    else:
        ls = string
        return ls


def digital_root1(n):
    return n if n < 10 else digital_root1(sum(map(int, str(n))))


def digital_root2(n):
    while n > 9:
        n = sum(map(int, str(n)))
    return n


if __name__ == '__main__':
    num = 132189
    res = digital_root1(34567890)
    # res = sum(map(int, str(678)))
    print(res)
