from concurrent.futures import ProcessPoolExecutor
from validate_prime import is_prime, PRIMES

def use_process():
    with ProcessPoolExecutor(max_workers=4) as executor:
        ans = executor.map(is_prime, PRIMES)
        return ans

if __name__ == '__main__':
    from timeit import repeat
    print('Time Avg:', min(repeat(
        'use_process()',
        setup='from __main__ import use_process', number=3)) / 3)
