# 斐波那契数列


def fib(n):
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a

# 使用递归
def fib_recursion(n):
    if n == 1 or n == 2:
        return 1
    return fib_recursion(n - 1) + fib_recursion(n - 2)



# 输出了第10个斐波那契数列
print(fib(10))
