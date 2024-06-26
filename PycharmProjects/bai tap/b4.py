def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def count_primes(A, B):

    count = 0
    for num in range(A, B + 1):
        if is_prime(num):
            count += 1
    return count


A = int(input("Nhập giá trị A: "))
B = int(input("Nhập giá trị B: "))


prime_count = count_primes(A, B)


print(f"Số lượng số nguyên tố trong khoảng [{A}, {B}] là: {prime_count}")
