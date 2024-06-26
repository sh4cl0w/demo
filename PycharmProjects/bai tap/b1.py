import math

def is_prime(N):
    diem = 0
    for i in range(1, N+1):
        if N % i == 0:
            diem += 1
    return diem

def is_qrime(N):
    qprime = []
    for i in range(1, N+1):
        diem = is_prime(i)
        if diem == 4:
            qprime.append(i)
    return qprime


if __name__ == '__main__':
    N = int(input())
    n=len(is_qrime(N))
    if(n==0):
        print("No")
    else:
        print(is_qrime(N))



