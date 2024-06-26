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

def is_powerful_number(num):
    primes = arraylist(int(num ** 0.5) + 1)
    for p in primes:
        if num % p == 0:
            if num % (p * p) != 0:
                return False
    return True

def array_powerful(N):
    powerful_numbers = []
    for i in range(1, N):
        if is_powerful_number(i):
            powerful_numbers.append(i)
    return powerful_numbers

# Số N cho trước
N = 10000
result = array_powerful(N)
print(result)
