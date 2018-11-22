import yaml
import os

class YamlReader:
    def __init__(self, yamlf):
        if os.path.exists(yamlf):
            self.yamlf = yamlf
        else:
            raise FileNotFoundError('文件不存在')
        self.__data = None

    def data(self):
        #如果第一次调用data则读取yaml文档，否则直接返回之前保存的数据
        if not self.__data:
            with open(self.yamlf, 'rb') as f:
                self.__data = list(yaml.safe_load_all(f))#load后是个generator，用list组织成列表
        return self.__data

