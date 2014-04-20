from concurrent.futures import ThreadPoolExecutor
from validate_prime import is_prime, PRIMES

def use_thread():
    with ThreadPoolExecutor(max_workers=4) as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            # print('%d is prime: %s' % (number, prime))
            pass

if __name__ == '__main__':
    from timeit import timeit
    print('Time Avg:', min(repeat(
        'use_thread()',
        setup='from __main__ import use_thread', number=3)) / 3)
