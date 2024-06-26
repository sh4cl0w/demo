"b34: Cài đặt thuật toán kiểm tra số nguyên tố Fermat. Trong trường hợp nào thì số nào thì thuật toán cho kết quả kiểm tra sai"
import random
import math

def power(a, b, c):
    result = 1
    a = a % c

    while b > 0:

        if b % 2 == 1:
            result = (result * a) % c
        b = b >> 1
        a = (a * a) % c

    return result

def fermat_test(p, t):
    if p <= 1 or p == 4:
        return 0
    if p <= 3:
        return 1

    random.seed(None)

    for i in range(t):
        a = 2 + random.randint(0, p - 4)  # Random number from [2, p-2]
        if power(a, p - 1, p) != 1:
            return 0
    return 1

if __name__ == "__main__":



    num = int(input("nhap N: "))
    t = int(input("lan lap: "))

    if fermat_test(num, t):
        print(f"{num} la so nguyen to")
    else:
        print(f"{num} khong la so nguyen to")

