def sieve_eratosthenes(N):
    is_prime = [True] * N
    is_prime[0] = is_prime[1] = False

    for p in range(2, int(N**0.5) + 1):
        if is_prime[p]:
            for i in range(p * p, N, p):
                is_prime[i] = False

    primes = [i for i, prime in enumerate(is_prime) if prime]
    return primes

def generate_primes_indefinitely():
    primes = []
    num = 2

    while True:
        is_prime = all(num % prime != 0 for prime in primes)
        if is_prime:
            yield num
            primes.append(num)
        num += 1

# Example usage to find primes less than 100
N = 100
primes_less_than_100 = sieve_eratosthenes(N)
print(primes_less_than_100)

# Example usage of the infinite prime generator
prime_generator = generate_primes_indefinitely()
for _ in range(10):  # Generate the first 10 prime numbers
    print(next(prime_generator))
