def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
def findX(A,B,C,m,l):
    array = []
    for x in range(m,l+1):

            value = A * x**2 + B * x + C
            if is_prime(value):
                array.append(x)
    return array
if __name__ == '__main__':
    A = int(input('Enter A: '))
    B = int(input('Enter B: '))
    C = int(input('Enter C: '))
    m = int(input('Enter m: '))
    l = int(input('Enter l: '))
    result = findX(A,B,C,m,l)
    for x in result:
        print(x)