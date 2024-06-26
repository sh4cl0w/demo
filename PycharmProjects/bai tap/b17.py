def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def findX(A,B,C):
    x=1
    while True:
        value = A * x**2 + B * x + C
        if is_prime(value):
            return x
        x+=1

if __name__ == '__main__':
    A = int(input('Enter A: '))
    B = int(input('Enter B: '))
    C = int(input('Enter C: '))
    result = findX(A,B,C)
    print(result)
