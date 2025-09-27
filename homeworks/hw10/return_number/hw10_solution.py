def check_int(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not isinstance(result, (int, float)):
            raise ValueError("Arguments should be a number")
        return result
    return wrapper


@check_int
def concat_str(a, b):
    return a + b


@check_int
def arguments_summary(a=0, b=0):
    return a + b
