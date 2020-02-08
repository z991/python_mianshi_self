"""
列出1到20的数字，若是3的倍数就用apple代替，若是5的倍数就用orange代替，若既是3的倍数又是5的倍数就用appleorange代替
"""

result = ['apple'[n % 3 * 5::] + 'orange'[n % 5 * 6::] or n for n in range(1, 21)]
print(result)
