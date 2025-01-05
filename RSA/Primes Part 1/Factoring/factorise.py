from sympy import factorint

N = 510143758735509025530880200653196460532653147

factors = factorint(N)
primes = sorted(factors.keys())
smaller_prime = primes[0]

print(smaller_prime)
