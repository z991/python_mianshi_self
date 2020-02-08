"""
编写一个函数将名称转换为首字母。这个kata严格地用两个词，它们之间有一个空格。
输出应该是两个大写字母，并用点分隔它们。
"""


def abbrevName(s_name: str) -> str:
    s_name = "Sam Harris"
    ls = s_name.split(" ")
    res = ".".join([i[0].upper() for i in ls])
    return res


def shangzi(name):
    return '.'.join(w[0] for w in name.split()).upper()


res = lambda name: ".".join(e[0].upper() for e in name.split())
