import os
import pytest
from common.excel_utls import ExcelUtil
from common.ini_utils import Config
from config.moudle import BASEDIR


class Run(object):
    # DATA = ExcelUtil().handel_data('all')  # 运行全部项目用例
    DATA = ExcelUtil().handel_data('正常')  # 运行冒烟（正常）用例
    # DATA = ExcelUtil().handel_data('测试用例2.xlsx', '登录')  # 指定项目和模块运行
    # DATA = ExcelUtil().handel_data('测试用例2.xlsx')  # 指定项目运行
    env_ini = '%s/config/env_host.ini' % BASEDIR

    def __init__(self):

        pass

    def run(self):
        # 先指定环境，写入配置文件
        env_ini = Run.env_ini
        Config(env_ini).write_varables('env', 'env', 'dev')

        # 运行用例
        pytest.main(['-v','--html=/Users/dongshuai/PycharmProject/pytest_practice/output/report/report.html'])

        # 生成allure测试报告
        # os.system('cp /Users/dongshuai/PycharmProject/pytest_practice/environment.properties /Users/dongshuai/PycharmProject/pytest_practice/output/allure/report')
        os.system('allure generate %s/output/allure/temp -o %s/output/allure/report --clean' % (BASEDIR, BASEDIR))


# print(Run.DATA)


if __name__ == '__main__':
    Run().run()

