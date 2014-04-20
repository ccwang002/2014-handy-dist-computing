from timeit import repeat
from validate_prime import is_prime, PRIMES

def orig_way():
    [is_prime(prime) for prime in PRIMES]

def my_bench(exec_stmt, setup, rpt=3, num=3):
     return min(repeat(
         exec_stmt, setup=setup,
         number=num, repeat=rpt)) / num

if __name__ == '__main__':
    print('Testing Orig / Multi Thread or Process')
    print('Minimum time average of 3 in 3 repeats')
    print('Orig:', my_bench(
        'orig_way()', 'from __main__ import orig_way'))
    print('Multithread:', my_bench(
        'use_thread()', 'from demo_multithread import use_thread'))
    print('Multiprocess:', my_bench(
        'use_process()', 'from demo_multiprocess import use_process'))

