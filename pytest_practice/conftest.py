import os

import pytest
from common.ini_utils import Config
from config.moudle import BASEDIR


# 指定运行环境
env = Config('%s/config/env_host.ini' % BASEDIR).read_variables('env', 'env')
@pytest.fixture(params=[env])
def env(request):
    return request.param

# 用例运行前后置的操作
@pytest.fixture(scope='module', autouse=True)
def setup_teardown(request):
    variable_ini = '%s/config/variable.ini' % BASEDIR  # 保存变量文件

    # 1.所有用例运行前，清空variable.ini中[response]下的变量
    options = Config(variable_ini).get_options('response')
    print("运行前操作:\n1.删除response下的optons变量%s" % options)
    if options:
        for option in options:
            Config(variable_ini).rm_option('response', option)

    # 2.运行前删除allure报告
    print('2.删除上次的allure报告的temp文件')
    temp_files = os.listdir('%s/output/allure/temp' % BASEDIR)
    # print(temp_files)
    for temp_file in temp_files:
        path = os.path.join('%s/output/allure/temp' % BASEDIR, temp_file)
        os.remove(path)

    yield
    print("\n运行后操作:\n暂无。")



