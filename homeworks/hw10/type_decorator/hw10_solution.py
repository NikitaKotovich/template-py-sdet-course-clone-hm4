def typed_checker(type_):
    def decorator(func):
        def wrapper(*args):
            new_args = []
            for arg in args:
                new_args.append(type_(arg))
            return func(*new_args)
        return wrapper
    return decorator


@typed_checker(str)
def add_str(a, b):
    return a + b


@typed_checker(float)
def add_float(*args):
    result = 0
    for arg in args:
        result += arg
    return result


@typed_checker(int)
def add_int(*args):
    return sum(args)
