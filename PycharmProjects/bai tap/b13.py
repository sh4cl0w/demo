import math

def soNT(n):

    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def array(n):

    primes = []
    for i in range(2, n + 1):
        if soNT(i):
            primes.append(i)
    return primes
def find(n):

    primes = array(n)
    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            p1, p2 = primes[i], primes[j]
            sum_of_primes = p1 + p2
            diff_of_primes = abs(p1 - p2)
            if soNT(sum_of_primes) and soNT(diff_of_primes):
                return p1, p2
    return None
if __name__ == '__main__':
    n = int(input())
    print(find(n))