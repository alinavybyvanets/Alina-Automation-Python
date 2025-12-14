def even_numbers(n):
    for i in range(0,n + 1, 2):
        yield i
N = 12
for num in even_numbers(N):
    print(num)

def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b
N = 10
for num in fibonacci(N):
    print(num)