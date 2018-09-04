
# последовательность Фибоначчи без рекурсии (занимает много памяти)

import time


def fibonacci(n):

    """ функция вычесления последовательности Фибонччи без рекурсии """

    arr = []

    a = 0
    b = 1

    for i in range(0, n-1):
        a, b = b, a + b
        arr.append(a)
    arr.insert(0, 0)
    return arr


start_time = time.time()

n = 100
print(fibonacci(n))

print('Время:', time.time() - start_time)
