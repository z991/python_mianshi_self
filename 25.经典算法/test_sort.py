import random
import operator

a = [
    {"num1": random.randint(1, 10), "num2": random.randint(1, 10)},
    {"num1": random.randint(1, 10), "num2": random.randint(1, 10)},
    {"num1": random.randint(1, 10), "num2": random.randint(1, 10)},
    {"num1": random.randint(1, 10), "num2": random.randint(1, 10)},
    {"num1": random.randint(1, 10), "num2": random.randint(1, 10)},
    {"num1": random.randint(1, 10), "num2": random.randint(1, 10)},
    {"num1": random.randint(1, 10), "num2": random.randint(1, 10)},
    {"num1": random.randint(1, 10), "num2": random.randint(1, 10)},
    {"num1": random.randint(1, 10), "num2": random.randint(1, 10)},
]
print('aaa====', a)
result = sorted(a, key=operator.itemgetter("num1", "num2"), reverse=True)

print('result=====', result)
