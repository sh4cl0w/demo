a=int(input("enter a:"))
b=int(input("enter b:"))
w,t=8,4

def chuyen_so_thanh_mang(a,t,w):
    arr=list()
    while t>0:

        arr.append(int( a/2**((t-1)*w)))
        a=a%2**((t-1)*w)
        t-=1
    return arr
arrA=chuyen_so_thanh_mang(a,t,w)
arrA.reverse()
arrB=chuyen_so_thanh_mang(b,t,w)
arrB.reverse()
c=list()
e=0

tmp=arrA[0]+arrB[0]
if tmp > 2**w:
    c.append(tmp%(2**w))
    e=1
else:
    c.append(tmp)
    e=0
for i in range(1,t):
    tmp = arrA[i] + arrB[i]+e
    if tmp > 2 ** w:
        c.append(tmp % (2 ** w))
        e = 1
    else:
        c.append(tmp)
        e = 0
c.reverse()
tup=tuple((e,c))
print(tup)
print(a+b)

#2902461432
#3791651136