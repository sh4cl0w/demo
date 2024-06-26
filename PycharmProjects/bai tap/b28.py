def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
def gcd(a, b):

    while b:
        a, b = b, a % b
    return a

def is_carmichael(n):

    if is_prime(n):
        return False
    for b in range(2, n):
        if gcd(b, n) == 1:
            if pow(b, n-1, n) != 1:
                return False
    return True

def find_carmichael_numbers(limit):

    array = []
    for n in range(2, limit):
        if is_carmichael(n):
            array.append(n)
    return array


N = int(input("Nhập N (0 <= N <= 10000): "))
if 0 <= N <= 10000:
    carmichael_numbers = find_carmichael_numbers(N)
    print("Các số Carmichael nhỏ hơn", N, "là:")
    print(carmichael_numbers)
else:
    print("Giá trị N không hợp lệ. Vui lòng nhập lại.")
