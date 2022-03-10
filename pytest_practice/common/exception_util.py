import json
import traceback
from functools import wraps

# 自定义异常装饰器
def cuntom_exception(reason=None):
    def exception(fun):
        @wraps(fun)
        def wrappers(*args, **kwargs):
            # noinspection PyBroadException
            try:
                return fun(*args, **kwargs)
            except Exception:
                print("出现异常：%s" % reason, traceback.format_exc())

        return wrappers
    return exception
