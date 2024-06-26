import random
def power(a, b, c):
    result = 1
    a = a % c

    while b > 0:

        if b % 2 == 1:
            result = (result * a) % c
        b = b >> 1
        a = (a * a) % c

    return result
def miller_rabin_test(d, n):
    """Thực hiện một bước kiểm tra Miller-Rabin"""
    a = random.randint(2, n - 2)
    x = power(a, d, n)

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

def main():
    N = int(input("Nhập giá trị N (0 < N < 1000): "))
    p = int(input("Nhập giá trị p (số nguyên tố): "))

    valid_a_values = []
    for a in range(1, N):
        result = power(a, p, N)
        if is_prime_miller_rabin(result,5):
            valid_a_values.append(a)

    print("Các số nguyên a < N sao cho a^p mod N là số nguyên tố:")
    print(valid_a_values)

if __name__ == "__main__":
    main()
