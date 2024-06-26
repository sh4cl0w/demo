import math


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def array(n):
    arraylist =[]
    for i in range(n):
        if(is_prime(i)):
            arraylist.append(i)
    return arraylist
def main():
    N = int(input())


    primes = array(N)
    prime_count = len(primes)


    for i in range(prime_count - 3):
        p1, p2, p3, p4 = primes[i], primes[i+1], primes[i+2], primes[i+3]
        sum_of_primes = p1 + p2 + p3 + p4
        if sum_of_primes <= N and is_prime(sum_of_primes):
            print(p1)
            print(p2)
            print(p3)
            print(p4)
            return

if __name__ == "__main__":
    main()