import json
import os

import openpyxl
from config.moudle import BASEDIR


class ExcelUtil(object):

    def __init__(self):
        self.keys = ('id', 'svr_name', 'case_name', 'path', 'method', 'headers', 'payloads', 'extract',
                     'priority', 'describe', 'validate')

    # 读取excel，处理数据返回列表
    def read_excel(self, excel_file) -> dict:
        wb = openpyxl.load_workbook(excel_file)
        sheets = wb.sheetnames

        result = dict()

        for sheet in sheets:
            ws = wb[sheet]
            values = list(ws.values)
            values.pop(0)
            # print(values)
            # print(sheet)
            value_list = []  # 存放模块下所有的用例列表
            for value in values:
                value_zip = list(zip(self.keys, value))
                value_dict = {k: v for k, v in value_zip}  # 字典生成式
                value_list.append(value_dict)

                result[sheet] = value_list
            # print(value_list)
        # print(result)
        return result


    # 往excel写入数据
    def write_excel(self, content, excel_file):
        pass

    # 用于指定项目、模块运行
    def handel_data(self, *args) ->list:
        # 格式校验
        if len(args) <= 0:
            raise Exception("请输人正确的运行用例范围，如：全部-->all，项目-->project，项目、模块-->project, module1, module2")

        all_cases = []  # 全部用例，格式[{},{},{}]
        excel_files = os.listdir('%s/data/excelcases' % BASEDIR)  # 用例文件 【文件1， 文件2】
        excel_files.pop(excel_files.index('__init__.py'))

        # 运行全部项目用例
        if args[0] in ['all', '全部']:
            # 获取所有excel用例文件目录
            for excel_file in excel_files:
                path = '%s/data/excelcases/%s' % (BASEDIR, excel_file)
                result_values = list(self.read_excel(path).values())
                # print(result_values)
                for result_value in result_values:
                    for value in result_value:
                        all_cases.append(value)
            return all_cases

        # 运行全部冒烟（正常）用例
        elif args[0] in ['冒烟', '正常']:
            print('走冒烟')
            # 获取所有excel用例文件目录
            for excel_file in excel_files:
                path = '%s/data/excelcases/%s' % (BASEDIR, excel_file)
                result_values = list(self.read_excel(path).values())
                # print(result_values)
                for result_value in result_values:
                    for value in result_value:
                        # print(value)
                        if '冒烟' in value['case_name'] or '正常' in value['case_name']:
                            all_cases.append(value)
            print("all cases：\n", all_cases)
            return all_cases


        # 根据项目、模块自定义选择运行
        else:
            if args[0] not in excel_files:
                raise Exception('%s项目excel文件不存在，请核实！', args[0])
            else:
                path = '%s/data/excelcases/%s' % (BASEDIR, args[0])
                result = self.read_excel(path)
                print(result)
                result_new = {}
                args_modules = args[1:]
                # print(args)
                result_keys = list(result.keys())

                # print(result_keys)
                if len(args_modules) == 0:   # 指定项目运行(运行项目下的全部)
                    result_values = list(result.values())
                    for result_value in result_values:
                        for case in result_value:
                            all_cases.append(case)
                else:   # 指定项目-模块运行
                    for arg in args_modules:
                        if arg not in result_keys:
                            raise Exception('%s项目中不存在模块%s' % (args[0], arg))
                        else:
                            result_new[arg] = result[arg]

                    result_values = list(result_new.values())

                    for result_value in result_values:
                        for value in result_value:
                            # print(value)
                            all_cases.append(value)

            # print("all cases：\n", all_cases)
            return all_cases

        # 根据接口名，或接口id，运行指定的接口：todo







# if __name__ == '__main__':
#     excel_path = '%s/data/excelcases/测试用例2.xlsx' % BASEDIR
#     # ExcelUtil().read_excel(excel_path)
#     ExcelUtil().handel_data('测试用例2.xlsx', '模块1', '模块2', '模块3')
    # ExcelUtil().handel_data('all')

# a = ['aa', "bb", "cc"]
# b = ["dd", 'ee', 'ff']
# # print(a + b)
# print(list(zip(a, b)))
#
# c = {x:y for x, y in list(zip(a, b))}
#
# print(c)
#
# print(list(c.values()))


#
# def aa(*args):
#
#     print(args)
#     print(args[0])
#
#
# aa(1)


# excel_files = os.listdir('%s/data/excelcases' % BASEDIR)
# excel_files.pop(excel_files.index('__init__.py'))
# print(excel_files)


# a = [1,2,3]
# b = (1,)
#
# print(b in a)
#
#
# aaa = (1,2,3,4,5,6)
# print(aaa[1:])
