
#    try:
#        return x/y
#    except ZeroDivisionError:
#       return None


def zero_div_handler_decorator(func):
    def wrapper(*args, **kwargs):               #Т.е. принимает любые переданные аргументы
        x, y = args
        if y == 0:
            return None
        return func(*args, **kwargs)
    return wrapper


@zero_div_handler_decorator
def div(x, y):
    return x / y

#decorated_div = zero_div_handler_decorator(div)

print(div(4, 2))
print(div(4, 0))