def twice(fn):
    def wrapper(x):
        print('Wrapped')
        value = fn(x)
        return value * 2
    return wrapper


@twice
def func(x):
    return x


print(func(3.14))
