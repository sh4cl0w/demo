import math
import random


def timUCLN(a, b):
    while b > 0:
        tmp = a % b
        a = b
        b = tmp
    return a
    # e nguyen to cung nhau voi an

def sang(n):
    arr=list()
    for i in range(2,n+1):
        arr.append(i)
    for i in range(len(arr)-1):
        j=i+1
        while j<len(arr):
            if arr[j]%arr[i]==0:
                arr.pop(j)
            else:
                j+=1
    return arr
arr=sang(500)
def kiemtranguyento(n,arr):
    if n==1 or n==0:
        return 0
    for i in arr:
        if n==i:
            return 1
        if n%i==0:
            return 0
    return 1
def randompq(arr):
    while 1:
        tmp=random.randrange(100,500)
        if kiemtranguyento(tmp,arr):
            return tmp

p=randompq(arr)
q=randompq(arr)

n=p*q
an=(p-1)*(q-1)
print(p,q,an)
def randome(an):
    while 1:
        e= random.randrange(1,100)
        if timUCLN(e,an)==1:
            return e
e=randome(an)
print("e=",e)
def euclid(a,b):
    tmp=b
    if b==0:
        x=1
        y=0
    x2,x1,y2,y1=1,0,0,1
    while b>0:
        q=int(a/b)
        r=a-(q*b)
        x=x2-(q*x1)
        y=y2-(q*y1)
        a=b
        b=r
        x2=x1
        x1=x
        y2=y1
        y1=y
    x=x2
    if x<0:
        x = x+tmp
    return x

d=euclid(e,an)
print("d=",d)
m=190411+123

def thuatToanNhanBiinhPhuongCoLap(a,k,n):
    def convert(num):
        i = 1
        arr = list()

        while num > 0:
            arr.append(num % 2)
            num = int(num / 2)
            i += 1
        return arr

    arrk = convert(k)
    A=a
    b=1
    if k==0:
        return b
    else:
        if arrk[0]==1:
            b=a
        for i in range(1,len(arrk)):
            A=(A*A)%n
            if arrk[i]==1:
                b=(A*b)%n
    return b

c=thuatToanNhanBiinhPhuongCoLap(m,e,n)

m=thuatToanNhanBiinhPhuongCoLap(c,d,n)

print("c=",c)
print("m=",m)