from concurrent.futures import ThreadPoolExecutor
from validate_prime import is_prime, PRIMES

def use_thread():
    with ThreadPoolExecutor() as executor:
        ans = executor.map(is_prime, PRIMES)
        return ans

if __name__ == '__main__':
    from timeit import repeat
    print('Time Avg:', min(repeat(
        'use_thread()',
        setup='from __main__ import use_thread', number=3)) / 3)
