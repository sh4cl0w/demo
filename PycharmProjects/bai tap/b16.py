import random

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
def array(n):
    arraylist = []
    for i in range(n):
        arraylist.append(random.randint(0, 100))
    return arraylist

def main():
    N = int(input("Nhập kích thước của mảng: "))

    # Sinh mảng ngẫu nhiên với kích thước N, các phần tử là số nguyên từ 0 đến 100
    random_array = array(N)

    print("Mảng ngẫu nhiên đã sinh:", random_array)

    # Tìm các số nguyên tố trong mảng
    prime_numbers = [num for num in random_array if is_prime(num)]

    print("Các số nguyên tố trong mảng là:", prime_numbers)

if __name__ == "__main__":
    main()
