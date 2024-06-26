import math


def soNT(n):

    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def uoc(n) :
    dem2=0
    for i in range(2, n+1):
        if (n % i == 0):
           dem2+=1
    return dem2
def demNT(n):
    dem1=0
    for i in range(2, n+1):
        if (soNT(i)):
            dem1+=1
    return dem1
if __name__ == "__main__":
    n = int(input())

    print(demNT(n))
    print(uoc(n))