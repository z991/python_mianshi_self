# names = 'Kunpen Ji, Li XIAO, Caron Li, Donl SHI, Ji ZHAO, Fia YUAN Y, Weue DING, Xiu ' \
#         'XU, Haiying WANG, Hai LIN, Jey JIANG, ' \
#         'Joson WANG E, Aiyang ZHANG, Hay MENG, Jak ZHANG E, Chang Zhang, Coro ZHANG'

from collections import OrderedDict
import operator

names=(' Kunpen Ji, Li XIAO, Caron Li,'
       ' Dongjian SHI, Ji ZHAO, Fia YUAN Y,'
       ' Wenxue DING, Xiu XU, Haiying WANG, Hai LIN,'
       ' Jey JIANG, Joson WANG E,'
       ' Aiyang ZHANG, Haiying MENG,'
       ' Jack ZHANG E, Chang Zhang, Coron ZHANG')

"""
问题1：排序,按照姓名A-Z排序

问题2：找出里面姓”ZHANG”有几个

问题3：找出名字里面最长的人
"""


class DealName:

    def sort_name(self, names):
        li = names.split(',')
        result = sorted(li)
        return result
    def len_zhang(self, str):
        result = []
        names_list = names.split(',')
        print(names_list)
        for name in names_list:
            for n in name.split():
               if n.lower() == "zhang":
                   result.append(name)
        return len(result)
    def max_len(self, str):
       names_list = names.split(',')
       len_n = 0
       for name in names_list:
            print(name, len(name))
            if len(name.strip()) > len_n:
                result = [name.strip()]
                len_n = len(name.strip())
            elif len(name) == len_n:
                result.append(name.strip())
       return result
   

if __name__ == '__main__':
    deal_name = DealName()
    r1 = deal_name.sort_name(names)
    r2 = deal_name.len_zhang(names)
    r3 = deal_name.max_len(names)
    pass
