import os
from utils.file_reader import YamlReader

#通过当前文件的绝对路径，其父级目录一定是框架的base目录，然后确定各层的绝对路径。
#将直接拼接的方法修改，使用os.path.split()和os.path.join()拼写路径，这样可以支持不同平台，例如linux和windows
BASE_PATH = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
CONFIG_FILE = os.path.join(BASE_PATH, 'config', 'config.yml')
DATA_PATH = os.path.join(BASE_PATH, 'data')
DRIVER_PATH = os.path.join(BASE_PATH, 'drivers')
LOG_PATH = os.path.join(BASE_PATH, 'log')
REPORT_PATH = os.path.join(BASE_PATH, 'report')

class Config:
    def __init__(self, config= CONFIG_FILE):
        self.config = YamlReader(config).data
    def get(self, element, index= 0):
        '''

        :param element: 需要提取配置文件中的关键字名
        :param index: 如果yaml文件中分节了才需要用的这个参数
        :return: config文件中element值对应的值
        '''
        return self.config[index].get(element)