import math


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

N = int(input())

p = 0
s = 0
q = 0
k = 0

for i in range(1, N + 1):
    if N % i == 0:
        p += i
        s += 1
        if is_prime(i):
            q += i
            k += 1

result = N + p + s - q - k
print(result)

