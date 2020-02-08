

def create_phone_number1(number_list):
    number_list.insert(0, '(',)
    number_list.insert(4, ') ',)
    number_list.insert(8, '-')
    return ''.join(map(str, number_list))


def create_phone_number(number_list):
    return '({}{}{}) {}{}{}-{}{}{}{}'.format(*number_list)


def create_phone_number2(n):
    n = ''.join(map(str, n))
    return '(%s) %s-%s' %(n[:3], n[3:6], n[6:])


if __name__ == '__main__':
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    result = create_phone_number1(number_list)
    print(result)