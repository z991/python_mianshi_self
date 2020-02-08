"""
编写一个迷你的计算器,支持两个数的加减乘除
"""

import re


class Calculator:

    def verify_num(self, n):
        # 用正则判断集中数字,正数，负数,小数
        patt = re.compile(r'^(-?\d+)(\.\d+)?$')
        return True if re.match(patt, n) else False

    def verify_opt(self, opt):
        # 运算符号验证
        return opt in ['+', '-', '*', '/']

    def mini_calculator(self):
        # 用户输入数据
        my_input = input('请输入两个数字和一个运算符,例如 1,2,+:\n')
        try:
            args = my_input.split(',')
            if len(args) == 3:
                a, b, opt = args
                if not self.verify_num(str(a)) or not self.verify_num(str(b)) or not self.verify_opt(opt):
                    print('输入格式错误')
                    return
                res = eval('{}{}{}'.format(a, opt, b))
                print('{}{}{}={}'.format(a, opt, b, res))
            else:
                print('输入参数长度必须为3')
        except ValueError as e:
            print('Value error', e)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    Calculator().mini_calculator()
