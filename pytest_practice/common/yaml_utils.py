import yaml
# 读取yaml，返回列表

from config.moudle import BASEDIR
from common.excel_utls import ExcelUtil


def read_yaml(yaml_path) ->dict:
    with open(yaml_path) as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value

# 写入yaml
def write_yaml(yaml_path, content):
    with open(yaml_path, 'w') as f:
        yaml.dump(data=content, stream=f, allow_unicode=True, sort_keys=False)






'''
写一个handel，处理下面为可迭代的有序列表，可根据自定义选择模块来进行生成，传值给parameters
'''
content = {
    "moudel1": [{"url": "", "headers": "", "payloads": "", "validate": ""}, {"url": "", "headers": "", "payloads": "", "validate": ""}, {}],
    "moudel2": [{"url": "", "headers": "", "payloads": "", "validate": ""}, {"url": "", "headers": "", "payloads": "", "validate": ""}, {}],
    "moudel3": [{"url": "", "headers": "", "payloads": "", "validate": ""}, {"url": "", "headers": "", "payloads": "", "validate": ""}, {}]
}

if __name__ == '__main__':
    # write_yaml(file_path="%s/data/caseyaml/testyaml.yaml" % BASEDIR, content=content)
    # print(read_yaml(yaml_path="%s/data/caseyaml/testyaml.yaml" % BASEDIR))

    data = ExcelUtil().read_excel('/Users/dongshuai/PycharmProject/pytest_practice/data/excelcases/测试用例2.xlsx')
    write_yaml(yaml_path="%s/data/caseyaml/testyaml.yaml" % BASEDIR, content=data)
