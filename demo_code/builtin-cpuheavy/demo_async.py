from concurrent.futures import ProcessPoolExecutor
from validate_prime import is_prime, PRIMES
from time import sleep

executor = ProcessPoolExecutor()
future_ans = [executor.submit(is_prime, p) for p in PRIMES[:6]]

while not all(future.done() for future in future_ans):
    print('do sth else, waiting')
    sleep(1)

print([f.result() for f in future_ans])
