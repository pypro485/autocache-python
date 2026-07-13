def make_key(func, args, kwargs):
    return (
        func.__module__,
        func.__name__,
        args,
        tuple(sorted(kwargs.items()))
    )