import json
import re
import traceback
import jsonpath
import requests
from all import Run
from common.ini_utils import Config
from config.moudle import BASEDIR
from custom_func import CustomFunc


# 根据环境，选择对应的域名
def url_util(host_dev, svr_name, path)->str:
    if host_dev == 'dev':
        host = Config(Run.env_ini).read_variables('host-dev', svr_name)
    elif host_dev == 'test':
        host = Config(Run.env_ini).read_variables('host-test', svr_name)
    else:
        host = Config(Run.env_ini).read_variables('host-yace', svr_name)

    url = 'http://%s%s' % (host, path)

    return url

# 接口请求封装
def req_util(url, method, headers, payloads)->str:
    if method == 'get':
        res = requests.request('get', url, headers=eval(headers), data=json.dumps(eval(payloads)))
        return res.text
    elif method == 'post':
        res = requests.request('post', url, headers=eval(headers), data=json.dumps(eval(payloads)))
        return res.text
    else:
        print('目前只支持get 和 post ！')


# 参数引用${variable}、${func()}
def quote(headers, payloads)->tuple:
    """re.sub()进行动态替换"""
    """
    1.re.findall() 匹配到所有的${} 和 ${func()} 各返回一个列表，
    2.检查是否存在于ini配置文件中，存在则re.sub替换，重新赋值给新的headers或payloads变量
    3.用反射的方式检查类中是否有这个方法，有则执行，返回结果，然后再re.sub替换，重新赋值给headers或payloads变量
    """

    # 正则匹配到所有引用变量列表，格式如：['random()', 'token', 'name']
    headers_virables_quotes = re.findall(r'\$\{(.*?)\}', headers)
    payloads_virables_quotes = re.findall(r'\$\{(.*?)\}', payloads)

    valiadate_ini = '%s/config/variable.ini' % BASEDIR


    # 对headers的操作
    for hvq in headers_virables_quotes:
        if hvq.endswith('()'):
            # 进行反射操作
            if hasattr(CustomFunc(), hvq[:-2]):
                fun = getattr(CustomFunc(), hvq[:-2])
                value = fun()
                headers = headers.replace('${%s}' % hvq, "\'%s\'" % value)  # 注意：header的value必须都是字符串
            else:
                raise Exception('没有找到对应变量${%s}' % hvq)
        else:
            # 在ini文件中判断是否存在变量
            if Config(valiadate_ini).has_option('custom', hvq):
                quote_value = Config(valiadate_ini).read_variables('custom', hvq)
                headers = headers.replace('${%s}' % hvq, quote_value)
            elif Config(valiadate_ini).has_option('response', hvq):
                quote_value = Config(valiadate_ini).read_variables('response', hvq)
                headers = headers.replace('${%s}' % hvq, quote_value)
            else:
                raise Exception('没有找到对应变量${%s}' % hvq)

    # 对payloads的操作
    for pvq in payloads_virables_quotes:
        if pvq.endswith('()'):
            # 进行映射操作
            if hasattr(CustomFunc(), pvq[:-2]):
                fun = getattr(CustomFunc(), pvq[:-2])
                value = fun()
                payloads = payloads.replace('${%s}' % pvq, str(value))
            else:
                raise Exception('没有找到对应变量${%s}' % pvq)
        else:
            # 在ini文件中判断是否存在变量
            if Config(valiadate_ini).has_option('custom', pvq):
                quote_value = Config(valiadate_ini).read_variables('custom', pvq)
                payloads = payloads.replace('${%s}' % pvq, quote_value)
            elif Config(valiadate_ini).has_option('response', pvq):
                quote_value = Config(valiadate_ini).read_variables('response', pvq)
                payloads = payloads.replace('${%s}' % pvq, quote_value)
            else:
                raise Exception('没有找到对应变量${%s}' % pvq)

    return headers, payloads


# 提取参数
def extract(extract, res_text):
    vaiable_ini = '%s/config/variable.ini' % BASEDIR
    try:
        if extract and isinstance(eval(extract), dict):
            extract = eval(extract)
            print(type(res_text))
            for k, v in extract.items():
                value = str(jsonpath.jsonpath(json.loads(res_text), '$..%s' % v))[1:-1]  # jsonpath进行模糊匹配
                Config(vaiable_ini).write_varables(section='response',
                                                   option=extract.get(k),
                                                   value=value
                                                   )
    except NameError:
        print('返回参数提取异常：', traceback.format_exc())




