import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
def is_perfect_cube(n):
    m = round(n ** (1/3))
    return m ** 3 == n
def reverse_number(n):

    return int(str(n)[::-1])

def find_perfect_cube():
    array =[]
    for i in range(100,1000):
        if is_prime(i):
            reverse1 = reverse_number(i)
            if is_perfect_cube(reverse1):
                array.append(i)

    return array
if __name__ == '__main__':
    array1 = find_perfect_cube()
    print(array1)