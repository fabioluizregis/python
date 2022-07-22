from itertools import count, islice
from filtering_comprehensions import is_prime


thousand_primes = islice((x for x in count() if is_prime(x)), 1000)
print(thousand_primes)
print(list(thousand_primes)[-10:])