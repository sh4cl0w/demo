def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
def binhphuong(limit):
    squares = []
    i = 1
    while i * i <= limit:
        squares.append(i * i)
        i += 1
    return squares
def arraylist(a,b):
    array = []
    for i in range(a,b+1):
        if(is_prime(i)):
            array.append(i)
    return array
def count1(a, b):

    S1 = binhphuong(a)
    S2 = binhphuong(b)
    print(S1)
    print(S2)
    primes = arraylist(a,b)

    count = 0
    for prime in primes:
        found = False
        for x in S1:
            if found:
                break
            for y in S2:
                if x + y == prime:
                    count += 1
                    found = True
                    break

    return count
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(count1(a,b))