# core i7 8750h, n=1000000 ~ 0,26s

import time


def find_primes(n):

    """ функция поиска простых чисел от 0 до n"""

    arr = set(range(n, 1, -1))
    primes = []
    while arr:
        p = arr.pop()
        primes.append(p)
        arr.difference_update(set(range(p*2, n+1, p)))
    return primes


start_time = time.time()

n = 1000000
primes = find_primes(n)

print('Время:', time.time() - start_time)
