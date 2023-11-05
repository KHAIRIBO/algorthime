#Module qui saisie le nombre de participant du club
def saisi_Nb_Part():
    global n
    n=int(input('donner le nombre des Participants : '))
    while(20<n<0):
        n=int(input('verifier le nombre des Participants : '))
def Saisie_Participant(n):
    global FSprt
    global Part
    FSprt=open("sport.txt","a")
    for i in range(n):
     Part={}
     Ident=dict(nom=str(),Prenom=str(),genre=str())
     info=dict(taille=int(),Poids=int())
     Adresse=dict(Num=int(),Rue=str(),Ville=str())
     print("Donner Identité du Participant"+str(i))
     Part["nom"]=input("saisir le Nom du joueur : ")
     while (len(Part["nom"])>20):
           Part["nom"]=input("verifier le Nom du joueur : ")
     Part["Prénom"]=input("saisir le Prénom du joueur: ")
     while (len(Part["Prénom"])>30):
           Part["Prénom"]=input("verifier le Prénom du joueur : ")
     Part["genre"]=input("saisir le genre du joueur : ")
     while (Part["genre"] not in ["M","F"]):
           Part["genre"]=input("verifier le genre du joueur : ")
     print("Donner les Informations du Participant"+str(i))
     Part["taille"]=int(input("saisir la taille du joueur :"))
     while(Part["taille"]<38 or Part["taille"]% 2 !=0):
           Part["taille"]=int(input("verifier la taille du joueur :"))
     Part["Poids"]=int(input("saisir le Poids du joueur : "))
     print("Donner Adresse du Participant"+str(i))
     Part["Num"]=int(input("saisir le Numero de rue du joueur : "))
     while (Part["Num"]<0):
           Part["Num"]=input("verifier le Numero du rue : ")
     Part["Rue"]=input("saisir la Rue : ")
     while (len(Part["Rue"])>40):
           Part["Rue"]=input("verifier la rue: ")
     Part["Ville"]=input("saisir la ville : ")
     while (len(Part["Ville"])>40):
           Part["Ville"]=input("verifier la Ville: ")      
     FSprt.write(Part["nom"]+" "+Part["Prénom"]+" "+Part["genre"])
     FSprt.write(str(Part["taille"])+" "+str(Part["Poids"]))
     FSprt.write(str(Part["Num"])+" "+Part["Rue"]+" "+Part["Ville"]+"\n")
    FSprt.close()
def Taille_Sup48():
    FSprt=open("sport.txt","r")
    ch=FSprt.readline()
    while(ch!=''):
        FSprt.close()
   
#P.P
saisi_Nb_Part()
Saisie_Participant(n)
FSprt=open("sport.txt","a")
Taille_Sup48()
FSprt.close()
