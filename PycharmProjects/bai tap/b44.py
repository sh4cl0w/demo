import math

arrA=input("enter array:").split()
arrA=[int(i) for i in arrA]
p=int(input("enter p:"))
def euclid(a,b):
    tmp=b
    if b==0:
        x=1
        y=0
    x2=1
    x1=0
    y2=0
    y1=1
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
        x=x+tmp
    return x

arrB=list()
for i in arrA:
    arrB.append(euclid(i,p))
print(arrA)
print(arrB)
