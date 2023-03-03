import os, sys

class XPath:
    @staticmethod
    def get_resource_path(path):
        if os.path.isabs(path):
            # 获取当前脚本所在目录的绝对路径
            dir_realpath = r'/Users/dchen/Documents/codemao/PushBoxGame'
            # 获取传入文件相对于脚本的相对路径
            relative_path = os.path.relpath(path, dir_realpath)
        else:
            relative_path = path
        if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)