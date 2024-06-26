import itertools
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
def arraylist(n) :
    array =[]
    for i in range(2,n+1):
        if is_prime(i):
            array.append(i)
    return array
def find_prime_sum(N, M):
    primes = arraylist(N)

    for combination in itertools.combinations(primes, M):
        if sum(combination) == N:
            return combination
    return None
if __name__ == '__main__':
    N = int(input())
    M = int(input())
    result = find_prime_sum(N, M)
    print(result)