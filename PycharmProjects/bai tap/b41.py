import random
def is_prime(n, k=5):
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

def mod_exp(a, k, n):
    result = 1
    a = a % n
    while k > 0:
        if (k % 2) == 1:
            result = (result * a) % n
        k = k >> 1
        a = (a * a) % n
    return result

def main():
    a = int(input("Nhập giá trị a (0 < a < 1000): "))
    k = int(input("Nhập giá trị k (0 < k < 1000): "))
    n = int(input("Nhập giá trị n (0 < n < 1000): "))

    result = mod_exp(a, k, n)
    print(f"{a}^{k} mod {n} = {result}")

    if is_prime(result):
        print(f"{result} là số nguyên tố.")
    else:
        print(f"{result} không phải là số nguyên tố.")

if __name__ == "__main__":
    main()
