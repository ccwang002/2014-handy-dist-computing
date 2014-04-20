import math

with open('prime_list.txt') as f:
    PRIMES = [int(l) for l in f]

def is_prime(n):
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def orig_way():
    ans = [is_prime(prime) for prime in PRIMES]
    return ans

if __name__ == '__main__':
    from timeit import repeat
    print('Time Avg:', min(repeat(
        'orig_way()',
        setup='from __main__ import orig_way', number=3)) / 3)
