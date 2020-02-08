"""
编写一）个函数，它以非负整数（秒）作为输入，并以人类可读的格式返回时间（HH:MM:SS）
Test.assert_equals(make_readable(60), "00:01:00")
Test.assert_equals(make_readable(86399), "23:59:59")
"""

def make_readable(number):
    if number < 0 or number >359999:
        return "请输入一个小于359999的非负整数"
    hour = number // 3600
    min_z = number % 3600
    min_r = min_z // 60
    sec = min_z % 60
    return '%02d:%02d:%02d' %(hour, min_r, sec)


def make_readable1(s):
 return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)



if __name__ == '__main__':
    result = make_readable(3500)
    print(result)
