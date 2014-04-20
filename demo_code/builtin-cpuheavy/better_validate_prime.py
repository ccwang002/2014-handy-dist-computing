from concurrent.futures import ProcessPoolExecutor
from validate_prime import PRIMES
import math


def better_is_prime(n):
    if n == 2 or n == 3:
        return True
    elif n < 2 or n % 2 == 0:
        return False
    elif n < 9:
        return True
    elif n % 3 == 0:
        return False
    r = int(math.sqrt(n + 1))
    f = 5
    while f <= r:
        if n % f == 0 or n % (f + 2) == 0:
            return False
        else:
            f += 6

    return True

def better_process():
    with ProcessPoolExecutor() as executor:
        ans = executor.map(better_is_prime, PRIMES)
        return ans

if __name__ == '__main__':
    from timeit import repeat
    print('Time Avg:', min(repeat(
        'use_process()',
        setup='from demo_multiprocess import use_process', number=3)) / 3)
    print('Better Alg Time Avg:', min(repeat(
        'better_process()',
        setup='from __main__ import better_process', number=3)) / 3)
