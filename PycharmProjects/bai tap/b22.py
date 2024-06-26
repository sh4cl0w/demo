def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
def F(n):
    if is_prime(n):
        return n
    else:
        return 0

def sum(L,R):
    sum = 0
    for i in range(L,R):
        for j in range(i+1,R+1):
            sum += F(i) * F(j)
    return sum
if __name__ == '__main__':
    L = int(input())
    R = int(input())

    result = sum(L,R)
    print(result)
