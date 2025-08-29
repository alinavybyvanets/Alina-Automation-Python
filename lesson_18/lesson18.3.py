def logger(func):
    def wrapper(*args, **kwargs):
        print (f'Виклик {func.__name__} з аргументами: {args}, {kwargs}')
        result = func(*args, **kwargs)
        print (f'Результат {result}')
        return result
    return wrapper
@logger
def add(a, b):
    return a + b

@logger
def sub(a, b):
    return a - b
@logger
def greet (name):
    return f'Hello, {name}'

add (3,4)
sub (5,4)
greet("Alina")

def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f'Помилка у фeнкції {func.__name__}: {e}')
            return "Error"
    return wrapper
@exception_handler
def divide(a, b):
    return a / b
print(divide(3,4))
print(divide(5,0))

