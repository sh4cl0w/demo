import math


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def gcd(a, b):
    return math.gcd(a, b)


def input_array():
    n = int(input("Nhập số lượng phần tử của mảng: "))
    A = []
    for i in range(n):
        num = int(input("Nhập phần tử: "))
        A.append(num)
    return A


def find_prime_gcd(A):
    array=[]
    n = len(A)
    for i in range(n):
        for j in range(i + 1, n):
            if is_prime(gcd(A[i], A[j])):
                array.append((A[i], A[j]))
    return array


def main():
    A = input_array()
    pairs = find_prime_gcd(A)
    if pairs:
        print("Các cặp số có GCD là số nguyên tố:")
        for pair in pairs:
            print(pair)
    else:
        print("Không có cặp số nào có GCD là số nguyên tố.")
    n= len(pairs)
    print(f"mang co {n} cap co GCD la nguyen to",)

if __name__ == "__main__":
    main()
