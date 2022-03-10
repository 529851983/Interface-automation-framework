import allure
import pytest
from all import Run
from common.request_util import req_util, url_util, quote, extract
from custom_func import CustomFunc


class TestCase:
    @pytest.mark.parametrize("args", Run.DATA)
    def test_all(self, args, env):
        """
        用例描述呀
        """
        # allure报告优化
        allure.dynamic.title(args['case_name'])
        allure.dynamic.feature('xxx项目')
        allure.dynamic.story('功能名称')
        allure.dynamic.description(args['describe'])
        allure.dynamic.severity(args['priority'])
        allure.dynamic.tag(CustomFunc().random())


        svr_name = args.get('svr_name')
        path = args.get('path')
        url = url_util(env, svr_name, path)
        method = args.get('method')
        validate = args.get('validate')

        # 引用变量
        headers, payloads = quote(args.get('headers'), args.get('payloads'))

        print(payloads)
        print('\n'+'当前运行环境为：'+env)

        # 请求接口
        res_text = req_util(url, method, headers, payloads)

        # 参数提取
        extract(args.get('extract'), res_text)

        # 断言校验
        print('接口id：%s' % args['id'])
        print('预期结果%s：%s' % (type(validate), validate))
        print('实际结果%s：%s' % (type(res_text), res_text))
        assert validate  in res_text
