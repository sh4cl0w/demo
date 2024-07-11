
# a=int(input("enter a:"))
# p=int(input("enter p:"))

def euclid(a,p):
    b=p
    if b==0:
        x=1
        y=0
    x1=0
    x2=1
    y1=1
    y2=0
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
        x+=p

    return x

print(euclid(550,1759))
