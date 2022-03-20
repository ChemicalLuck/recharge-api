from functools import wraps


def recharge_v1(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        self.headers['X-Recharge-Version'] = '2021-01'
        return func(*args, **kwargs)
    return wrapper


def recharge_v2(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        self.headers['X-Recharge-Version'] = '2021-11'
        return func(*args, **kwargs)
    return wrapper
