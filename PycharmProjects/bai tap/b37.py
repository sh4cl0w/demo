s1=input("enter xau s1:")
s2=input("enter xau s2:")

def kiemtre(a,b):
    for i in range(len(a)):
        if a[i]!=b[i]:
            return 0
    return 1



def tinhFj(s1):
    fj=list()

    for i in range(0,len(s1)):

        if i==0:
            fj.append(-1)
        elif i==1:
            fj.append(0)
        else:
            count=0
            for x in range(1,i):
                a=''
                b=''
                for j in range(x):
                    a=a+s1[j]
                    b=s1[i-1-j]+b
                if kiemtre(a,b):
                    count=len(a)
            fj.append(count)

    return fj

fj=tinhFj(s1)
print(fj)
def tim(fj,s1,s2):
    i=j=0
    h=0
    while 1:

        if s1[j]!=s2[i+h]:
            i=i+j-fj[j]
            h=0
            if fj[j]==-1:
                j=0
            else:
                j=fj[j]
        else:
            h+=1
            j+=1
        if j>=len(s1):
            return i
        if i+h>=len(s2):
            return 0
print(tim(fj,s1,s2))