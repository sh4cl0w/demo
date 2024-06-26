def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def sum_of_primes_in_range(A, B):
    total = 0
    for num in range(A, B + 1):
        if is_prime(num):
            total += num
    return total

def main():
    A = int(input("Nhập số A: "))
    B = int(input("Nhập số B: "))

    total = sum_of_primes_in_range(A, B)

    if is_prime(total):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
