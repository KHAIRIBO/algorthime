from numpy import*
def saisirN():
    global n
    v=False
    while(v==False):
        n=int(input("saisir N : "))
        v=(5<=n<=15)
def remplirM(n):
    global m
    m=array([[int()]*n]*n)
    s=0
    i1=-1
    for i in range(n):
        if(i+1<=(n//2)+1):
            i1=i1+1
            i2=n-i
            for j in range(i1,i2):
                s=s+1
                m[i,j]=s
        else:
            s=s+1
            i1=i1-1
            i2=i2+1
            for j in range(i1,i2):
                m[i,j]=s
                s=s+1
def chaine(ch):
    p=0
    for i in range(len(ch)):
        if("0"<=ch[i]<="9"):
            p=i
    return ch[0:p+1]


def remplirF(nph,n,m):
    f=open(nph,"w")
    for i in range(n):
        ch=""
        for j in range(n):
            if(m[i,j]==0):
                ch=ch+""
            else:
                ch=ch+str(m[i,j])+""
        ch=chaine(ch)
        f.write(ch+"\n")
    f.close()
nph="resultat.txt"
saisirN()
remplirM(n)
remplirF(nph,n,m)
print(m)