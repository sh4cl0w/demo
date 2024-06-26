def power(a, b, c):
    result = 1
    a = a % c

    while b > 0:

        if b % 2 == 1:
            result = (result * a) % c
        b = b >> 1
        a = (a * a) % c

    return result
def mod_inverse(a, p):

    return power(a, p-2, p)

def main():
    p = int(input("Nhập giá trị p (số nguyên tố): "))
    A = list(map(int, input("Nhập các phần tử của mảng A (cách nhau bởi dấu cách): ").split()))

    B = [mod_inverse(a, p) for a in A]

    print("Mảng B có các phần tử là nghịch đảo của các phần tử tương ứng trong A:")
    print(B)

if __name__ == "__main__":
    main()
