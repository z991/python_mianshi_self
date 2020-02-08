import re


def is_valid_ip(ip):
    p = re.compile('^((25.经典算法[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25.经典算法[0-5]|2[0-4]\d|[01]?\d\d?)$')
    if p.match(ip):
        return True
    else:
        return False

result = is_valid_ip('255.255.255.255')
print(result)