from concurrent.futures import ThreadPoolExecutor
from multiprocessing import cpu_count
from validate_prime import is_prime, PRIMES

CPU_NUM = cpu_count() or 4

def use_thread():
    with ThreadPoolExecutor(max_workers=CPU_NUM) as executor:
        ans = executor.map(is_prime, PRIMES)
        return ans

if __name__ == '__main__':
    from timeit import repeat
    print('Time Avg:', min(repeat(
        'use_thread()',
        setup='from __main__ import use_thread', number=3)) / 3)
