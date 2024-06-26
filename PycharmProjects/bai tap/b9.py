def is_prime(n):

    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def count_primes(N):

    count = 0
    for num in range(2, N + 1):
        if is_prime(num):
            count += 1
    return count

# Nhập N từ bàn phím
N = int(input("Nhập giá trị N: "))

# Đếm số lượng số nguyên tố nhỏ hơn hoặc bằng N
prime_count = count_primes(N)

# In kết quả
print(f"Số lượng số nguyên tố nhỏ hơn hoặc bằng {N} là: {prime_count}")
