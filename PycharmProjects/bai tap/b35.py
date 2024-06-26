import random

def miller_rabin_test(d, n):
    """Thực hiện một bước kiểm tra Miller-Rabin"""
    a = random.randint(2, n - 2)
    x = pow(a, d, n)
    if x == 1 or x == n - 1:
        return True
    while d != n - 1:
        x = (x * x) % n
        d *= 2
        if x == 1:
            return False
        if x == n - 1:
            return True
    return False

def is_prime_miller_rabin(n, k):
    """Kiểm tra xem n có phải là số nguyên tố với xác suất cao sử dụng thuật toán Miller-Rabin"""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Tìm d và r sao cho n-1 = d * 2^r
    d = n - 1
    while d % 2 == 0:
        d //= 2

    # Thực hiện k lần kiểm tra
    for _ in range(k):
        if not miller_rabin_test(d, n):
            return False
    return True


N = int(input("Nhập số nguyên dương N: "))

k = 5

if is_prime_miller_rabin(N, k):
    print(f"Số {N} có khả năng là số nguyên tố với xác suất cao sau {k} lần kiểm tra Miller-Rabin.")
else:
    print(f"Số {N} không phải là số nguyên tố.")

