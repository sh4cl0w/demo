def is_prime(n):
    """Kiểm tra xem một số có phải là số nguyên tố hay không."""
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

def reverse_number(n):

    return int(str(n)[::-1])

def find_emirps(N):

    emirps = []
    for num in range(2, N):
        if is_prime(num):
            reversed_num = reverse_number(num)
            if is_prime(reversed_num):
                emirps.append(num)
    return emirps


N = int(input("Nhập giá trị N: "))


emirps = find_emirps(N)
print(f"Các số emirp nhỏ hơn {N} là: {emirps}")
