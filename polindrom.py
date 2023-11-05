
def sasir():
    global n
    val=False
    while val==False:
        n=int(input("donne nombre de mots : "))
        val=(1<=n<=20)

def chainr(ch):
    i=0
    ch1=ch.upper()
    while (i<len(ch)):
        if ("A"<=ch1[i]<="Z"):
            i=i+1
        else:
            return False
    return True
def dp(ch):
    i=0
    j=-1
    
    while (len(ch) //2)>i:
        if ch[i]==ch[j]:
            i=i+1
            j=j-1   
        else:
            return False
    return True
        
def rompler(n):
    f1=open("MOt.txt","w")
    for i in range(n):
        val=False
        while val==False:
            ch=str(input("done le  mots : "))
            val=((len(ch)<=15)and(chainr(ch)) )
            f1.write(ch)
        f1.write("\n")
    f1.close()
def affiche():
    f2=open("MOt.txt","r")
    for i in range (n): 
        t=f2.readline()
        if dp(t):
            print(t,end=":")
        else:
          print(" ")
    f2.close()






#P.P
sasir()
rompler(n)
