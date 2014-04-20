from concurrent.futures import ProcessPoolExecutor
from validate_prime import PRIMES

def better_is_prime(number):
    if number <= 1 or number % 2 == 0:
        return False
    check = 3
    maxneeded = number
    while check < maxneeded + 1:
        maxneeded = number / check
        if number % check == 0:
            return False
        check += 2
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
    print('Better Time Avg:', min(repeat(
        'better_process()',
        setup='from __main__ import better_process', number=3)) / 3)
