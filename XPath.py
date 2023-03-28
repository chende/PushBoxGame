
import sys
import os
import shutil

class XPath:
    def get_resource_path(self):
        relative_path = 'resources'

        resource_path = ''
        if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
            resource_path = os.path.join(sys._MEIPASS, relative_path)
        else:
            resource_path =  os.path.join(os.path.abspath("."), relative_path)

        print("resource path: " + resource_path)
        return resource_path

    def get_data_path(self):
        data_file = ''
        if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
            home_dir = os.path.expanduser('~')
            program_dir = os.path.join(home_dir, 'PushBoxGame')
            if not os.path.exists(program_dir):
                os.makedirs(program_dir)

            # 如果程序被打包成了可执行文件，提取数据文件到固定的数据文件夹中
            working_dir = sys._MEIPASS
            print("working dir: " + working_dir)
            source_data_file = os.path.join(working_dir, 'data/ranking.csv')
            data_file = os.path.join(program_dir, 'ranking.csv')
            if not os.path.exists(data_file):
                print("copy data to data dir: " + data_file)
                shutil.copyfile(source_data_file, data_file)
        else:
            # 否则，在当前目录中使用数据文件
            data_file = os.path.join(os.path.abspath("."), 'data/ranking.csv')

        print("data file path: " + data_file)
        return data_file

# 单例对象
instance = XPath()