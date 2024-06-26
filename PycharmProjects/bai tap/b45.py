import random

def is_prime(n, k=5): #Miller-Rabin
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Viết n-1 dưới dạng 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Thử k lần
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_prime_array(N):
    A = []
    num = 2
    while len(A) < N:
        if is_prime(num):
            A.append(num)
        num += 1
    return A

def min_distance(A):
    min_dist = float('inf')
    A_sorted = sorted(A)
    for i in range(1, len(A_sorted)):
        dist = A_sorted[i] - A_sorted[i - 1]
        if dist < min_dist:
            min_dist = dist
    return min_dist

# Nhập số lượng phần tử N từ bàn phím
N = int(input("Nhập số lượng phần tử của mảng A: "))

# Sinh mảng số nguyên tố A
A = generate_prime_array(N)

# In ra mảng A
print("Mảng A gồm các số nguyên tố là:", A)

# Tính và in ra khoảng cách nhỏ nhất giữa 2 số bất kỳ trong mảng A
min_dist = min_distance(A)
print("Khoảng cách nhỏ nhất giữa 2 số bất kỳ trong mảng A là:", min_dist)
