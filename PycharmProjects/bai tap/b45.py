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
    a = random.randint(2, n - 2)
    x = power(a, d, n)
    if x == 1 or x == n - 1:
        return True
    while d != (n - 1):
        x = (x * x) % n
        d *= 2
        if x == 1:
            return False
        if x == n - 1:
            return True
    return False


def is_prime(n, k):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    d = n - 1
    while d % 2 == 0:
        d = d // 2
    for i in range(k):
        if not miller_rabin_test(d, n):
            return False
    return True

def array(n):
    arraylist = []
    for i in range(n):
        p = generate_prime_in_range(1,1000)
        arraylist.append(p)
    return arraylist
def generate_prime_in_range(start, end):
    while True:
        num = random.randint(start, end)
        if is_prime(num,5):
            return num

def sort(numbers):

    length = len(numbers)

    for i in range(0, length - 1):
        for j in range(i + 1, length):
            if (numbers[i] > numbers[j]):
                # Hoán đổi vị trí
                tmp = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = tmp

    return numbers
def min_distance(A):
    min_dist = float('inf')

    A_sorted = sort(A)
    for i in range(1, len(A_sorted)):
        dist = A_sorted[i] - A_sorted[i - 1]
        if dist < min_dist:
            min_dist = dist
    return min_dist

# Nhập số lượng phần tử N từ bàn phím
N = int(input("Nhập số lượng phần tử của mảng A: "))

# Sinh mảng số nguyên tố A
A = array(N)
array_list = [num for num in A if is_prime(num,5)]

# In ra mảng A
print("Mảng A gồm các số nguyên tố là:", array_list)

# Tính và in ra khoảng cách nhỏ nhất giữa 2 số bất kỳ trong mảng A
min_dist = min_distance(A)
print("Khoảng cách nhỏ nhất giữa 2 số bất kỳ trong mảng A là:", min_dist)
