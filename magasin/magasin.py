from pickle import dump,load
e=dict(nom=str,qte=int,prix=float,etat=str)
def rempler():
    global n
    fc=open("comonde.dat","wb")
    rep="oui"
    n=0
    while rep=="oui":
        n+=1
        print("Article numero : "+str(n))
        e={}
        val=False
        while val==False:
      
            e["nom"]=str(input("donle le nom : "))
            val=len(e["nom"])>2
        val=False
        while val==False:
           
            e["qte"]=int(input("donne le qontete : "))
            val=(e["qte"])>0
        val=False
        while val==False:
       
            e["prix"]=float(input("donne le prix : "))
            val=e["prix"]>0
        val=False
        while val==False:
         
            e["etat"]=str(input("donne le etat : "))
            val=(e["etat"]=="vrai" or e["etat"]=="faux")
        dump(e,fc)
        print("ajoute autre article ? ")
        val=False
        while val==False:
    
            rep=str(input(" oui or no :"))
            val=(rep=="oui")or (rep=="no")
        val=(rep=="no")
    fc.close()
def remplerfact():
    t=0
    fc=open("comonde.dat","rb")
    fa=open("factuer.txt","w")
    for i in range (n):
        ch=""
        e=load(fc)
        if(e["etat"]=="faux"):
            ch=e["nom"]+" : "+str(e["qte"]*e["prix"])
            t=t+(e["qte"]*e["prix"])
            fa.write(ch+"\n")
        
    fa.write("total est : "+str(t))
    fa.close()
    fc.close()



def afiichage():
    fa=open("factuer.txt","r")
    ch=fa.readline()
    while ch!="":
        print(ch)
        ch=fa.readline()



#P.P
rempler()
remplerfact()
afiichage()