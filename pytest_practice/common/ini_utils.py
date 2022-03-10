import configparser


class Config(object):
    """
    对ini文件进行读写等操作
    """

    def __init__(self, file_ini):
        # 初始化
        self.file_ini = file_ini
        self.config = configparser.ConfigParser()
        self.config.read(file_ini, encoding='utf-8')

    # 获取section下全部的options
    def get_options(self, section):
        return self.config.options(section)


    # 读取section下的某个options
    def read_variables(self, section, option):
        value = self.config.get(section, option)
        return value

    # 往某个section下写入或编辑options
    def write_varables(self, section, option, value=None):
        self.config.set(section, option, value)
        self.config.write(open(self.file_ini, 'w'))

    # 删除section
    def rm_section(self, section):
        self.config.remove_section(section=section)
        self.config.write(open(self.file_ini, 'w'))

    # 删除section下的options
    def rm_option(self, section, option):
        self.config.remove_option(section=section, option=option)
        self.config.write(open(self.file_ini, 'w'))

    # 判断是否存在section
    def has_section(self, section):
        return self.config.has_section(section)

    # 判断是否存在option
    def has_option(self, section, option):
        return self.config.has_option(section=section, option=option)








# filename = '/Users/dongshuai/PycharmProject/pytest_practice/config/env_host.ini'

if __name__ == '__main__':
    filename = '/Users/dongshuai/PycharmProject/pytest_practice/config/variable.ini'
#     # 读取option
#     value = Config(filename).read_variables('env', 'name')
#     print(value)

    # 写入options
    # Config(filename).write_varables(filename,'env', 'env', 'yace')

    # Config(filename).rm_section('bbb')

    print(Config(filename).get_options('custom'))


