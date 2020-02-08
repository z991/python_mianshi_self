
# def is_validip(ip):
#     if len(ip) < 1:
#        return 'False'
#     if len(ip.split('.')) != 4:
#         return 'False'
#     for i in ip.split('.'):
#         i = i.strip()
#
#         if i.isdigit(): # 判断是否为数字类型
#             if i != '0' and i.startswith('0'): # 如果不为0
#                 return 'False'
#             if int(i) not in range(0, 256):
#                 return 'False'
#         else:
#             return 'True'
#     return 'True'
import random
r = random.randint(1, 7)
import string
def verrify_each(ip_addr):
    if len(ip_addr)>1 and ip_addr.startswith('0'):return False
    for c in ip_addr:
        if c in string.digits:
            continue
        elif c in string.ascii_letters:
            return False
        else:
            return False

    else:
        return True if int(ip_addr)<=255 and int(ip_addr)>=0 else False

def is_valid_IP(ip_str):
    ip_list = ip_str.split('.')
    if len(ip_list) != 4:
        return False
    res = [verrify_each(each) for each in ip_list]
    return True if all(res) else False



# if __name__ == '__main__':
    # ip_list = ['01.02.03.04', '12.255.56.1', 'abc.def.ghi.jkl',
    #            '123.456.789.0', '12.34.56', '12.34.56 .1','12.34.56.-1',
    #            '123.045.067.089', '127.1.1.0', '0.0.0.0', '0.34.82.53',
    #            '192.168.1.300'
    #            ]
    # for ip in ip_list:
    #     result = is_validip(ip)
    #     print('{}:{}'.format(ip, result))
