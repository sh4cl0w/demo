

def chuyen_so_thanh_mang(a,t,w):
    arr=list()
    while t>0:

        arr.append(int( a/2**((t-1)*w)))
        a=a%2**((t-1)*w)
        t-=1
    return arr
def solve(a,b,w,t ):

    arrA=chuyen_so_thanh_mang(a,t,w)
    arrA.reverse()
    arrB=chuyen_so_thanh_mang(b,t,w)
    arrB.reverse()

    c = []
    epsilon = 0
    e = pow(2, 8)
    for i in range(t):
        s = arrA[i] + arrB[i] + epsilon
        x = s%e
        if(s > e): epsilon = 1
        else: epsilon = 0
        c.append(x)
    return (epsilon, c[::-1])
if __name__=='__main__':
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    w,t=8,4
    print(solve(a,b,w,t))


#2902461432
#3791651136
