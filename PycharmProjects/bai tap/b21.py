def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
def count_primes(n):
    count = 0
    for i in range(2, n):
        if is_prime(i):
            count += 1
    return count
def is_super_prime(A,B):
    count = 0
    for X in range(A, B + 1):
        prime_count = count_primes(X)
        if is_prime(prime_count):
            count += 1
    return count

if __name__ == "__main__":
    A = int(input("Enter A: "))
    B = int(input("Enter B: "))

    n= is_super_prime(A,B)
    print(n)