s1=input("nhap chuoi s1:")
s2=input("nhap chuoi s2:")

def lti(a,n):
    for i in range(len(a)-1,0-1,-1):
        if a[i]==n:
            return i
    return -1
def tim(s1,s2):
    m=len(s2)
    i=j=m-1

    while j>=0:
        if i>=len(s1):
            return -1
        if s1[i]==s2[j]:
            i-=1
            j-=1
        else:
            i=i+m-min(j,1+lti(s2,s1[i]))
            j=m-1
    return i+1
if tim(s1,s2)==-1:
    print("khong tin thay chuoi")
else:
    print(tim(s1,s2))