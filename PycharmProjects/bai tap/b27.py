import math
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
def gcd(a, b):

    while b:
        a, b = b, a % b
    return a


result = []


for a in range(1, 1000):
    for b in range(a + 1, 1000):
        g = gcd(a, b)
        if is_prime(g):
            result.append((a, b))
for i in result:
    print(i)
