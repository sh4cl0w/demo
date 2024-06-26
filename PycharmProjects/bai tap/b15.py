import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
def find_twin_primes(N):

    array = []
    for num in range(2, N-1):
        if is_prime(num) and is_prime(num + 2):
            array.append((num, num + 2))
    return array
if __name__ == '__main__':
    N = int(input())
    primes = find_twin_primes(N)
    print(primes)