from __future__ import division
import os
import copy

class DirFiles:

    def __init__(self):
        self.files_dict = dict()

    def get_fileSize(self, file):
        """
        获取单个文件的大小和名称
        :param file:
        :return:
        """
        if os.path.exists(file):
            size = os.path.getsize(file)
            self.files_dict[file] = size

    def list_fileSize(self, path='.'):
        """
        列出目录下所有的文件和子目录内的文件
        :param path:
        :return:
        """
        if not os.path.exists(path):
            print('path error')
            return None
        file = ''
        try:
            for file in os.listdir(path):
                filepath = os.path.join(path, file)
                if os.path.isdir(filepath):
                    print('dir=====', filepath)
                    self.list_fileSize(path=filepath)
                elif os.path.isfile(filepath):
                    print('isfile====', filepath)
                    self.get_fileSize(filepath)
        except TypeError:
            print(file)

    def displayFilesSize(self, files=[], size_KB=False, size_MB=False):
        """
        统计文件大小并按MB,KB显示
        :param files:
        :param size_KB:
        :param size_MB:
        :return:
        """
        if size_KB:
            return str(round(sum(files)/1024), 2)+'K'
        elif size_MB:
            return str(round(sum(files)/(1024*1024), 2))+'M'
        else:
            return str(round(sum(files),2))+'byte'


if __name__ == '__main__':
    mypath = r"/Users/zhuxuanyu/Documents"
    dir_files = DirFiles()
    dir_files.list_fileSize(mypath)

    all_files_size =dir_files.displayFilesSize(dir_files.files_dict.values(), size_MB=True)
    print('\nTotal>:files num={0}, size={1}\n'.format(len(dir_files.files_dict), all_files_size))

    if len(dir_files.files_dict)>1:
        new_files_dict = zip(dir_files.files_dict.values(), dir_files.files_dict.keys())
        new = copy.deepcopy(new_files_dict)

        print(min(new))
        print(max(new_files_dict))
