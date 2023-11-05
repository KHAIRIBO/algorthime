from numpy import*

def saisir():
    global n
    n=int(input("saisir les nombres de plates: "))
    while not (1<=n<=30):
         n=int(input("saisir les nombres de plates: "))

def verif(ch):
    i=0
    test=True
    v=False
    while(v==False):
        if not("A"<=ch[i].upper()<="Z") or (ch[i]==" "):
            test=False
        else:
            i=i+1
        v=(i==len(ch)-1) or (test==False)
    return test


def remplirT(n):
    res=dict(numa=int(),lib=str(),prix=float())
    global t
    t=array([res]*n)
    for i in range(n):
        t[i]={}
        t[i]["numa"]=i+1
        v=False
        while(v==False):
            t[i]["lib"]=str(input("saisir le libèlle" +str(i+1)+":  "))
            v=(verif(t[i]["lib"]) and (len(t[i]["lib"])<=20))
        v=False
        while(v==False):
            t[i]["prix"]=float(input("saisir Prix "+str(i+1)+":  "))
            v=t[i]["prix"]>0

def saisirN1():
    global n1
    v=False
    while(v==False):
        n1=int(input("saisir N1"))
        v=1<=n1<=100
def remplirM(n1,n):
    global m
    m=array([[int()]*10]*n1)
    for i in range(n1):
        for j in range (10):
            m[i,j]=0

    for i in range(n1):
        v=False
        while(v==False):
            x=int(input("Donner le nombre de demande : "))
            v=(1<=x<=10)
        for j in range(x):
            v=False
            while(v==False):
                m[i,j]=int(input("saisir le matrice : "))
                v=m[i,j]<=n



def total(m,t,n1):
    s=0
    i=0
    while(m[n1,i]!=0 and (i<=9)):
        s=s+t[m[n1,i]-1]["prix"]
        i=i+1
    return s





#p.p
saisir()
remplirT(n)
saisirN1()
remplirM(n1,n)
for i in range(n):
    print("Le total prix de client",str(i+1),"est",str(total(m,t,i)))
s=0
for j in range(n1):
    s=s+total(m,t,j)

print("le total de ",s)
