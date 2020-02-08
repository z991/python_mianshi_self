import os
path_root = '/Users/zhuxuanyu/Pictures/django/'
for root_file in os.listdir(path_root):
    path = path_root + root_file
    if os.path.isdir(path)==True and root_file != ".DS_Store":
        for file in os.listdir(path):
            new_name = root_file + "++" + file
            os.rename(os.path.join(path, file), os.path.join(path, new_name))