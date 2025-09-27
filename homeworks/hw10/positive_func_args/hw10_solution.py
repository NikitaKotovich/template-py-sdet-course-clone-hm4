def validate_arguments(func):
    def wrapper(*args, **kwargs):
        total = list(args) + list(kwargs.values())
        for i in total:
            if not isinstance(i, (int, float)) or i <= 0:
                raise ValueError(f"{i} is not a positive")
        return func(*args, **kwargs)
    return wrapper


@validate_arguments
def sum_positive(*args, **kwargs):
    return sum(args) + sum(kwargs.values())
