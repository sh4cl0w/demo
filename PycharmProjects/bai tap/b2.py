import math
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def find(N):

    min = 10**(N-1)
    max = 10**N -1
    primes = []

    for num in range(min, max + 1):
        if is_prime(num):
            primes.append(num)

    return primes


if __name__ == "__main__":
    N=int(input())

    n=find(N)
    print(n)