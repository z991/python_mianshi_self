import random

number = random.randint(1, 20)
n = 0
while True:
    if n == 5:
        print("game over")
        break
    num = input("请输入一个1~20的整数")
    try:
        num = int(num)
    except:
        continue
    if num == number:
        print("您猜对了")
        break
    elif num > number:
        print("输入的数字偏大")
        n += 1
    elif num < number:
        print("输入的数字偏小")
        n += 1

