def sum_of_divisors(number):
    # Tính tổng các ước của số number (trừ chính nó)
    total = 0
    for i in range(1, number):
        if number % i == 0:
            total += i
    return total

def find_amicable_numbers(N):
    amicable_pairs = []
    for a in range(1, N):
        b = sum_of_divisors(a)
        if b > a and sum_of_divisors(b) == a:
            amicable_pairs.append((a, b))
    return amicable_pairs

if __name__ == '__main__':

    N = int(input("Nhập số nguyên dương N: "))
    amicable_numbers = find_amicable_numbers(N)
    if amicable_numbers:
        for i in amicable_numbers:
            print(i)

