
# последовательность Фибоначчи без рекурсии (через генератор)

import time


def fib_calc(n):
    """функция расчета следующей последовательности Фибоначчи"""
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


def fibonacci(n):
    """функция получения последовательности Фибоначчи"""
    arr = []
    for x in fib_calc(n):
        arr.append(x)
    arr.insert(0, 0)
    return arr


start_time = time.time()

n = 100
print(fibonacci(n))

print('Время:', time.time() - start_time)
