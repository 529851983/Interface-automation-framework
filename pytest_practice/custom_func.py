import random
from common.exception_util import cuntom_exception

class CustomFunc(object):
    # 生成随机数
    @cuntom_exception('生成随机数异常！')
    def random(self):
        return random.randint(0, 9999)