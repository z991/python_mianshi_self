import os

path = "/Users/zhuxuanyu/Documents"


def num_file(path):
    files = []
    list_p = os.listdir(path)
    for l in list_p:
        l_path = os.path.join(path, l)
        if os.path.isdir(l_path):
            files.extend(num_file(l_path))
        if os.path.isfile(l_path):
            files.append(l_path)
    return files



if __name__ == '__main__':
    re = num_file(path)
    print(re)
    print(len(re))
