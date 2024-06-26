import math

def timUCLN(a, b):
    while b > 0:
        tmp = a % b
        a = b
        b = tmp
    return a
def find_gcd(M, N, D):
    array = []
    for A in range(M, N + 1):
        for B in range(M, N + 1):
            if timUCLN(A, B) == D:
                array.append((A, B))
    return array
if __name__ == '__main__':
    M = int(input())
    N = int(input())
    D = int(input())
    result = find_gcd(M, N, D)
    for i in result:
        print(i)