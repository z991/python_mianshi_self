import re
from collections import Counter

# with open("a.txt", "r", encoding="utf-8") as f:
#     texts = f.read()  # 将文件的内容全部读取成一个字符串
#     count = Counter(re.split(r"\W+", texts))  # 以单词为分隔
#
# result = count.most_common(10)  # 统计最常使用的前10个
# print(result)

from collections import Counter

file_path = 'a.txt'
count = Counter()

with open(file_path) as file:
    for item in file.readlines():
        count.update(Counter(item.split()))
print(count.most_common(10))

with open(file_path) as file_1:
    tmp_list1 = []
    for line in file_1.readlines():
        tmp_list = line.split('"')
        for index in range(len(tmp_list)):
            if (index + 1) % 2 != 0:
                tmp_list_handle = tmp_list[index].strip()
                tmp_list2 = tmp_list_handle.split()
                tmp_list1.extend(tmp_list2)
            else:
                tmp_list1.extend([tmp_list[index]])
    count1 = Counter(tmp_list1)
    print(count1.most_common(10))