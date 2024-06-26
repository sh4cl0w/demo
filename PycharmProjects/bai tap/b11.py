def sieve_of_eratosthenes(N):

    is_prime = [True] * (N + 1)
    p = 2
    while (p * p <= N):
        if is_prime[p]:
            for i in range(p * p, N + 1, p):
                is_prime[i] = False
        p += 1
    prime_numbers = [p for p in range(2, N + 1) if is_prime[p]]
    return prime_numbers

def sum_primes(N):

    primes = sieve_of_eratosthenes(N)
    return sum(primes)

# Nhập N từ bàn phím
N = int(input("Nhập giá trị N: "))


prime_sum = sum_primes(N)

# In kết quả
print(f"Tổng các số nguyên tố nhỏ hơn hoặc bằng {N} là: {prime_sum}")
