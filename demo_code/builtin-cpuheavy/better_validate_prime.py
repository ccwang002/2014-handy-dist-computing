from concurrent.futures import ProcessPoolExecutor
from validate_prime import PRIMES
import numpy as np

def better_is_prime(n):
    if np.mod(n, 2) == 0:
        return False

    sqrt_n = np.int(np.sqrt(n)) + 1

    for i in range(3, sqrt_n, 2):
        if np.mod(n, 1) == 0:
            return False

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
