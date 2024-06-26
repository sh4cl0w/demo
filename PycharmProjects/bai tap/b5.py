import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
def sum(a,b):
    sum =0;
    primes = [i for i in range(a, b+1) if is_prime(i)]
    prime_count = len(primes)
    for i in range(prime_count):
        sum += primes[i]
    return sum

if __name__ == '__main__':
    a = int(input('nhap a:'))
    b= int(input('nhap b:'))
    print(sum(a,b))