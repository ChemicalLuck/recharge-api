from functools import wraps


def recharge_v1(func):
    """Forces the 'X-Recharge-Version' header for methods only available for
        Recharge API version 1/2021-01"""
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        self.headers['X-Recharge-Version'] = '2021-01'
        response = func(*args, **kwargs)
        self.headers['X-Recharge-Version'] = self.version
        return response
    return wrapper


def recharge_v2(func):
    """Forces the 'X-Recharge-Version' header for methods only available for
        Recharge API version 1/2021-11"""
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        self.headers['X-Recharge-Version'] = '2021-11'
        response = func(*args, **kwargs)
        self.headers['X-Recharge-Version'] = self.version
        return response
    return wrapper
