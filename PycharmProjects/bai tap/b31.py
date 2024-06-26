def power(a, b, c):
    result = 1
    a = a % c

    while b > 0:

        if b % 2 == 1:
            result = (result * a) % c
        b = b >> 1
        a = (a * a) % c

    return result
def sieve_eratosthenes(limit):

    is_prime = [True] * (limit + 1)
    p = 2
    while (p * p <= limit):
        if (is_prime[p] == True):
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        p += 1
    prime_numbers = [p for p in range(2, limit + 1) if is_prime[p]]
    return prime_numbers

def find_nearest_prime(number, primes):

    closest_prime = primes[0]
    min_distance = abs(number - closest_prime)
    for prime in primes:
        distance = abs(number - prime)
        if distance < min_distance:
            closest_prime = prime
            min_distance = distance
        elif distance == min_distance and prime < closest_prime:
            closest_prime = prime
    return closest_prime


mssv = int(input("Nhập mã số sinh viên của bạn: "))

limit = 100000
primes = sieve_eratosthenes(limit)
nearest_prime = find_nearest_prime(mssv, primes)
print("Số nguyên tố gần nhất với phần số của MSSV là:", nearest_prime)


a = mssv
k = nearest_prime
n = 123456
result = power(a, k, n)
print(f"Kết quả của {a}^{k} mod {n} là:", result)
