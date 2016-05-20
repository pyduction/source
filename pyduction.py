#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import * 
from tkinter.messagebox import *
from tkinter.filedialog import *
import tkinter.font as tkFont
"""fenetre du programme"""
fenetre = Tk()
fenetre.configure(bg = "#cccccc")
fenetre.title("PyDuction")
def dimension(self,nl,nh,bool): # a utiliser seulement pour le contenu de la fenetre principale !!
    self.update_idletasks()
    global l
    global h
    l, h = self.winfo_screenwidth(), self.winfo_screenheight() #capture des dimensions de l'écran
    self.geometry("%dx%d+0+0" % (l//nl, h//nh)) #formater la fenetre en taille et en position
    self.resizable(width=bool, height=bool)
    print(l,h)
dimension(fenetre,1,1,TRUE)
"""liste, chaine-liste, paramètres invariables"""
global valeurbooléen
global nbligne
nbligne = 0
varliste = []
typeliste = ["int","float","str"]
interditstr = "&(§!çà^`ù=:;,<>@#?./+£%*¨°"
nbstr = "1234567890"
signeliste = ["<","≤",">","≥","==","!=","dans","est"]
#pas utile pour le moment.

"""menu fichier"""
def exporter(evenement=None):
    code=Text.get(zonepy,index1=1.0,index2='end')
    presentation=Text.get(zonepresentation,index1=1.0,index2='end')
    unicode="#!/usr/bin/env python3\n# -*- coding: utf-8 -*- \n"
    enregistrer=asksaveasfile(title="Sauvegarder une image",filetypes=[('python files','*.py'),('all files','.*')]
    ,initialfile="Nouveau",defaultextension='.py',parent=fenetre,typevariable=code)
    fichier = open(enregistrer.name,'a')
    fichier.write(unicode+"\"\"\"\n"+presentation+"\n\"\"\"\n"+code)
    fichier.close()
def ouvrir():    # En ouvre la première partie en python
    code=Text.get(zonepy,index1=1.0,index2='end')
    myFile=askopenfile(title="Ouvrir le fichier python",filetypes=[('texte files','*.txt')]
    ,initialfile="Nouveau",defaultextension='.py',parent=fenetre,typevariable=code)
    content = myFile.read()
    zonepy.insert(END, content)
                # En ouvre la deuxième partie en français
    code=Text.get(zonefr,index1=1.0,index2='end')
    myFile=askopenfile(title="Ouvrir le fichier traduit",filetypes=[('texte files','*.txt')]
    ,initialfile="Nouveau",defaultextension='.txt',parent=fenetre,typevariable=code)
    content = myFile.read()
    zonefr.insert(END, content)
def quitter(evenement=None):
    fenetre.destroy()
def enregistrer(): # En enregistre la première partie en python
    code=Text.get(zonepy,index1=1.0,index2='end')
    enregistrer=asksaveasfile(title="Enregistrer la partie python",filetypes=[('texte files','*.txt'),('all files','.*')]
    ,initialfile="Nouveau",defaultextension='.txt',parent=fenetre,typevariable=code)
    fichier = open(enregistrer.name,'a')
    fichier.write(code)
    fichier.close()
                  # En enregistre cette deuxième partie en français
    code=Text.get(zonefr,index1=1.0,index2='end')
    enregistrer=asksaveasfile(title="Enregistrer la partie traduite",filetypes=[('texte files','*.txt'),('all files','.*')]
    ,initialfile="Nouveau",defaultextension='.txt',parent=fenetre,typevariable=code)
    fichier = open(enregistrer.name,'a')
    fichier.write(code)
    fichier.close()
"""menu aide"""
def apropos():
    """Création du toplevel"""
    rideau = Toplevel()
    rideau.title("A Propos")
    dimension(rideau,4,2.7,FALSE)
    widgetdim(rideau)
    center(rideau)
    """création des variables"""
    Message(rideau,text="Créateur:\n\nDENARIE Tamatea\nLY Rainui\nTEHAMATAI Karl\n\n"
                        "Remerciements:\n\nM.CARILLO\nM.SOULON\nM.VIRIAMU\nMAROT Toerau\n\n"
                        "Alpha-testeurs:\n\nLAYTON Tahivai\nLOYAT-CADOUSTEAU Greg").grid(row=0,column=0)
def documentation():
    rideau= Toplevel()
    rideau.title("Afficher une variable")
    dimension(rideau,1,1,FALSE)
    center(rideau)
    widgetdim(rideau)
    """sous fonction"""
    msg1 = Message(rideau,width=widgetlargeur-10,text="Creer une variable\n\n")
    """positionnement"""
    msg1.grid(row=0,column=0)
"""utile"""
def center(self):
    self.update_idletasks()
    width = self.winfo_width()
    height = self.winfo_height()
    x = (self.winfo_screenwidth() // 2) - (width // 2)
    y = (self.winfo_screenheight() // 2) - (height // 2)
    self.geometry('{}x{}+{}+{}'.format(width, height, x, y))
def widgetdim(self): #connaitre les dimensions d'un widget
    l,h = self.winfo_width(),self.winfo_height()
    global widgetlargeur
    global widgethauteur
    widgetlargeur = l
    widgethauteur = h
    print(l,h)
def nligne():
    global nbligne
    nbligne += 1
    zoneligne.insert(END,"  {}\n".format(nbligne))
def rechercher(self, p):
    global valeurbooléen
    valeurbooléen = True
    for i in self:
        if i in p:
            print ("voila ce qu'il y a en commun: ", i)
            valeurbooléen = False
        else:
            pass
    print(valeurbooléen)
def alert():
    zonefr.insert(END,"hey papi\n"*20)
    zonepy.insert(END,"hey papi\n"*20)
    nligne()
def etat1():
    b3.configure(state="active")
    b2.configure(state="active")
    b4.configure(state="active")
def etat2():
    b11.configure(state="active") #indenter
def etat3():
    b12.configure(state="active") #supprimer
"""fonction #1 """
def creevariable(evenement=None):
    """Création du toplevel"""
    rideau = Toplevel()
    rideau.title("Créer une variable")
    dimension(rideau,2.5,5,FALSE)
    center(rideau)
    """sous-fonctions"""
    def bind(event):
        verifier()
    def verifier(): #event permet l'assignation des touches grâce à bind
        verifietype = spinvariable.get()
        verifievaleur = box2.get()
        verifienom = box.get()
        nomok = False
        global  valeurok
        valeurok = False
        typeok = True
        """Condition pour la valeur"""
        if verifietype == "int" or verifietype =="float":
            try:
                verifievaleur = float(verifievaleur)
                valeurok = True
            except:
                showerror("Erreur de valeur", 'Votre valeur doit être un nombre.\n'
                'Veuillez réessayer.')

        else:
            valeurok = True

        """Condition pour le nom"""
        rechercher(verifienom,interditstr)
        if verifienom[:1] in nbstr:
            showerror("Erreur de nom", 'Votre nom doit commencer par une lettre.\n'
            'Veuillez réessayer.')
        elif valeurbooléen == False:
            showerror("Erreur de nom", 'Votre nom ne doit pas contenir des caractères spéciaux.\n'
            'Veuillez réessayer.')
        else:
            nomok = True

        """Condition pour le type"""
        if verifietype == "int" or verifietype == "float" or verifietype == "str":
            typeok = True
        else:
            typeok = False

        """Condition pour effectuer la déclaration d'une variable"""
        if valeurok and nomok and typeok is True:
            print(valeurok,nomok,typeok) #aide
            confirmer()
        elif typeok is False:
            showerror("Erreur de type", 'Votre type de variable n\'est pas valable.\n'
            'Veuillez réessayer.')
            print(valeurok,nomok,typeok) #aide
    def confirmer():
        recupnom = box.get()
        recuptype = spinvariable.get()
        recupvaleur = box2.get()
        varliste.append(recupnom)
        print("type: ",typeliste,"nom: ",varliste)
        if recuptype == "int":
            zonepy.insert(END, "{} = {}({}) \n".format(recupnom,recuptype,recupvaleur))
            zonefr.insert(END, "Déclaration d'un entier: {} = {}\n".format(recupnom,recupvaleur))
        elif recuptype == "float":
            zonepy.insert(END, "{} = {}({}) \n".format(recupnom,recuptype,recupvaleur))
            zonefr.insert(END, "Déclaration d'un flottant: {} = {}\n".format(recupnom,recupvaleur))
        else:
            zonepy.insert(END, "{} = {}(\'{}\') \n".format(recupnom,recuptype,recupvaleur))
            zonefr.insert(END, "Déclaration d'une chaine de caractere: {} = {}\n".format(recupnom,recupvaleur))
        nligne()
        etat1()
        etat3()
        rideau.destroy()
    """variables tkinter permettant l'affichage graphique"""
    box = StringVar() #on instancie un objet de la classe StringVar() sur 'box' pour qu'il soit une variable tkinter.
    box2 = StringVar()
    spinvariable = StringVar()
    entreeNom = Entry(rideau, textvariable=box, width=11)
    spintype = Spinbox(rideau,values=typeliste,textvariable=(spinvariable),width=5)
    entreeValeur = Entry(rideau, textvariable=box2, width=15)
    creer = Button(rideau, text="Créer", command=verifier)
    """Position des variables tkinter"""
    Label(rideau, text='Remarque:',fg="red").grid(row=1,columnspan=2, column=0,padx=1,sticky=W)
    Label(rideau,text='   ›\"int\" représente les nombres entiers: 1,2,3 ...').grid(row=2,columnspan=7,sticky=W)
    Label(rideau,text='   ›\"float\" est l\'équivalent des nombres décimaux: 1.5, 3.14 ...').grid(row=3,columnspan=7,sticky=W)
    Label(rideau,text='   ›\"str\" représente des messages: \"J\'ai mangé 3 pommes\".').grid(row=4,columnspan=7,sticky=W)
    Label(rideau,text='   ›Les nombres à virgule s\'écrivent avec un point: \"1.750\".').grid(row=5,columnspan=7,sticky=W)
    Label(rideau, text='Nom').grid(row=0, column=0,padx=1,pady=5)
    Label(rideau, text='Type').grid(row=0, column=2,padx=1,pady=5)
    Label(rideau, text='Valeur').grid(row=0,column=4,padx=1,pady=5)
    entreeNom.grid(row=0,column=1,padx=2,pady=5)
    spintype.grid(row=0, column=3,padx=2,pady=5)
    entreeValeur.grid(row=0, column=5,padx=2,pady=5)
    creer.grid(row=0, column=6,padx=10,pady=5)
    """Assignation des touches"""
    spintype.bind("<Return>", bind)
    entreeValeur.bind("<Return>", bind)
    creer.bind("<Return>", bind)
def lirevariable(evenement=None):
    """Création du toplevel"""
    rideau = Toplevel()
    rideau.title("Lire une variable")
    dimension(rideau,4.3,6,FALSE)
    center(rideau)
    """Sous fonction"""
    def bind(event):
        confirmer()
    def confirmer():
        recupvar = spinvar.get()
        recuptype = spintype.get()
        recupmsg = box.get()
        if recupvar in varliste:
            zonepy.insert(END, "{} = {}(input(\"{}: \"))\n".format(recupvar,recuptype,recupmsg))
            zonefr.insert(END, "Lecture de {} du type {} suivant cette instruction \"{}\"\n".format(recupvar,recuptype,recupmsg))
            nligne()
            rideau.destroy()
        else:
            showerror('Erreur variable','La variable que vous avez renseigné n\'existe pas.\nVeuillez réessayer.')
    def aide():
        tringle = Toplevel()
        tringle.title("Lire une variable")
        dimension(tringle,4,6,FALSE)
        center(tringle)
        widgetdim(tringle)
        Label(tringle, text="Lire une variable.",fg="Red").grid(row=0,column=0,sticky=W)
        msg = Message(tringle,width=widgetlargeur-10,anchor='center',justify='left', text="Cette fonction permet à l'utilisateur de"
                                                        " choisir une valeur durant l'éxécution du script,"
                                                        " selon le type choisis, afin qu'elle soit"
                                                        " affecter à une variable propre à elle même")
        msg.grid(row=1, column=0,sticky=W)
    """Définition des variables"""
    spinvar = StringVar()
    spintype = StringVar()
    box = StringVar()
    variable = Spinbox(rideau,values=varliste,textvariable=spinvar,width=12)
    type = Spinbox(rideau, values=typeliste, textvariable=spintype, width=5)
    message = Entry(rideau,textvariable=box,width=20)
    aide = Button(rideau, text="Aide", command=aide)
    lire = Button(rideau, text="Lire", command=confirmer)
    """Position des variables"""
    Label(rideau, text="Type de variable: ").grid(row=1,column=0,sticky=W,pady=2)
    Label(rideau,text="Lire la variable: ").grid(row=0,column=0,sticky=W,pady=2)
    Label(rideau,text="Instruction: ").grid(row=2,column=0,sticky=W,pady=2)
    message.grid(row=2,column=1,padx=3,sticky=W,pady=2)
    variable.grid(row=0,column=1,padx=3,sticky=W,pady=2)
    type.grid(row=1,column=1, padx=3,sticky=W,pady=2)
    aide.grid(row=3,column=0, padx=2, sticky='W')
    lire.grid(row=3,column=1, padx=2, sticky='E')
    """Bind des variables"""
    message.bind("<Return>",bind)
    lire.bind("<Return>",bind)
def affecter(evenement=None):
    rideau = Toplevel()
    rideau.title("Affecter une valeur")
    dimension(rideau,2.15,5.2,FALSE)
    center(rideau)
    """Sous fonction"""
    def bind(event):
        confirmaff()
    def confirmaff():
        recupvaleur = box.get()
        recupvar = spinvar.get()
        if recupvar in varliste:
            zonepy.insert(END, "{} = {}\n".format(recupvar,recupvaleur))
            zonefr.insert(END, "La variable {} prend comme valeur: {}\n".format(recupvar,recupvaleur))
            nligne()
            rideau.destroy()
        else:
            showerror('Erreur variable','La variable que vous avez renseigné n\'existe pas.\nVeuillez réessayer.')
    """variables tkinter"""
    spinvar = StringVar()
    box = StringVar()
    variable = Spinbox(rideau,values=(varliste),textvariable=(spinvar),width=10)
    entree = Entry(rideau, textvariable=box, width=30)
    affecter = Button(rideau, text="Affecter", command=confirmaff)
    """placement des variables"""
    Label(rideau, text='Prend la valeur de ').grid(row=0,column=1,padx=5,pady=2,)
    variable.grid(row=0,column=0,padx=5,pady=2)
    entree.grid(row=0,column=2,padx=5,pady=2)
    affecter.grid(row=0,column=3,padx=5,pady=2)
    Label(rideau, text='Remarque:',fg="red").grid(row=1,columnspan=4,sticky=W)
    Label(rideau,text='   ›Python ne peux pas effectuer une addition entre deux variables de types différents').grid(row=2,columnspan=4,sticky=W)
    Label(rideau,text='   ›Python utilise les guillemets \" \" pour écrire une chaine de caractère.').grid(row=3,columnspan=4,sticky=W)
    Label(rideau,text='   ›Python peut dupliquer une chaine de caractère avec le signe \'*\'.').grid(row=4,columnspan=4,sticky=W)
    Label(rideau,text='   ›Python peut changer le type de votre variable.').grid(row=5,columnspan=4,sticky=W)
    """Bind des variables"""
    entree.bind("<Return>", bind)
    affecter.bind("<Return>",bind)
"""fonction #2"""
def affichervar(evenement=None):
    rideau= Toplevel()
    rideau.title("Afficher une variable")
    dimension(rideau,4.5,12,FALSE)
    center(rideau)
    """sous fonction"""
    def bind(event):
        confirmer()
    def confirmer():
        recupvar=spinvariable.get()
        if recupvar in varliste:
            zonepy.insert(END, "print({})\n".format(recupvar))
            zonefr.insert(END, "Affichage de la variable: {}\n".format(recupvar))
            nligne()
            rideau.destroy()
        else:
            showerror("Erreur variable","La variable que vous avez renseigné n\'existe pas.\nVeuillez réessayer.")
    """Définition des variables"""
    spinvariable = StringVar()
    variable = Spinbox(rideau,values=varliste,textvariable=spinvariable,width=15)
    afficher = Button(rideau,text="Afficher",command=confirmer)
    """Position des variables"""
    Label(rideau,text="Afficher la variable: ").grid(row=0,column=0,padx=2,pady=2)
    variable.grid(row=0,column=1,padx=2,pady=2)
    afficher.grid(row=1,columnspan=2,padx=2,pady=2,sticky=E)
    """Bind des variables"""
    afficher.bind("<Return>",bind)
    variable.bind("<Return>",bind)
    rideau.bind("<Return>",bind)
def affichertxt(evenement=None):
    rideau= Toplevel()
    rideau.title("Afficher un texte")
    dimension(rideau,4.5,12,FALSE)
    center(rideau)
    """sous fonction"""
    def bind(event):
        confirmer()
    def confirmer():
        recuptxt=box.get()
        if len(recuptxt) > 0:
            zonepy.insert(END, "print(\"{}\")\n".format(recuptxt))
            zonefr.insert(END, "Affichage du texte: {}\n".format(recuptxt))
            nligne()
            etat3()
            rideau.destroy()
        else:
            showerror("Erreur", "Vous n'avez entré aucun texte.\nVeuillez réessayer.")
    """Définition des variables"""
    box = StringVar()
    txt = Entry(rideau,textvariable=box,width=18)
    afficher = Button(rideau,text="Afficher",command=confirmer)
    """Position des variables"""
    Label(rideau,text="Afficher le texte: ").grid(row=0,column=0,padx=2,pady=2)
    txt.grid(row=0,column=1,padx=2,pady=2)
    afficher.grid(row=1,columnspan=2,padx=2,pady=2,sticky=E)
    """Bind des variables"""
    afficher.bind("<Return>",bind)
    txt.bind("<Return>",bind)
    rideau.bind("<Return>",bind)
def afficherclc(evenement=None):
    rideau= Toplevel()
    rideau.title("Afficher un calcul")
    dimension(rideau,4.5,12,FALSE)
    center(rideau)
    """sous fonction"""
    def bind(event):
        confirmer()
    def confirmer():
        recupclc=box.get()
        if len(recupclc) > 0:
            zonepy.insert(END, "print({})\n".format(recupclc))
            zonefr.insert(END, "Affichage du calcul: {}\n".format(recupclc))
            nligne()
            etat3()
            rideau.destroy()
        else:
            showerror("Erreur", "Vous n'avez entré aucun calcul.\nVeuillez réessayer.")
    """Définition des variables"""
    box = StringVar()
    clc = Entry(rideau,textvariable=box,width=18)
    afficher = Button(rideau,text="Afficher",command=confirmer)
    """Position des variables"""
    Label(rideau,text="Afficher le calcul: ").grid(row=0,column=0,padx=2,pady=2)
    clc.grid(row=0,column=1,padx=2,pady=2)
    afficher.grid(row=1,columnspan=2,padx=2,pady=2,sticky=E)
    """Bind des variables"""
    afficher.bind("<Return>",bind)
    clc.bind("<Return>",bind)
    rideau.bind("<Return>",bind)
"""fonction #3"""
def sisinon(evenement=None):
    rideau= Toplevel()
    rideau.title("SI...SINON...")
    dimension(rideau,3.2,10,FALSE)
    center(rideau)
    """sous fonction"""
    def bind(event):
        confirmer()
    def confirmer():
        recupvariable = spinvar.get()
        recupsigne = spinsigne.get()
        recupvaleur = box.get()
        zonefr.insert(END,"Si {} {} {} alors:\n".format(recupvariable,recupsigne,recupvaleur))
        zonepy.insert(END,"If {} {} {}:\n".format(recupvariable,recupsigne,recupvaleur))
        nligne()
        etat2()
        etat3()
        rideau.destroy()
    def verifier():
        recupvariable = spinvar.get()
        recupsigne = spinsigne.get()
        variableok = False
        signeok = False
        if recupvariable in varliste:
            variableok = True
        else:
            showerror("Erreur de variables","La variable que vous avez choisis n'existe pas\nVeuillez recommencer.")
        if recupsigne in signeliste:
            signeok = True
        else:
            showerror("Erreur de signes","Le signe que vous avez choisis n'existe pas.\nVeuillez recommencer.")
        if variableok is True and signeok is True:
            confirmer()
    def aide():
        tringle = Toplevel()
        tringle.title("SI...SINON...")
        dimension(tringle,4,5,FALSE)
        center(tringle)
        widgetdim(tringle)
        police = tkFont.Font(family="Helvetica",size=24,weight="bold")
        Label(tringle, text="SI...SINON...",fg="Red").grid(row=0,column=0,sticky=W)
        msg = Message(tringle,width=widgetlargeur-10,anchor='center',justify='left', text="Cette fonction permet à l'utilisateur d'imposer"
                                                        " une condition à son programme.\n"
                                                        "Exemple:\n\tSi 'a' > 5 alors\n\ton ajoute 2 à 'a'\n\t"
                                                        "Sinon,\n\ton soustrait 4 à 'a'")
        msg.grid(row=1, column=0,sticky=W)
    def sinon():
        zonefr.insert(END,"Sinon:\n")
        zonepy.insert(END,"else:\n")
        rideau.destroy()
    """Définition des variables"""
    spinvar = StringVar()
    spinsigne = StringVar()
    box = StringVar()
    variable = Spinbox(rideau,values=varliste,textvariable=spinvar,width=12)
    signe = Spinbox(rideau, values=signeliste, textvariable=spinsigne, width=5)
    entree = Entry(rideau, textvariable=box, width=12)
    aide = Button(rideau, text="Aide", command=aide)
    ok = Button(rideau,text="ok",command=verifier)
    sinon = Checkbutton(rideau,text='SINON',command=sinon)
    """Position des variables"""
    Label(rideau,text="SI").grid(row=0,column=0,padx=2,pady=2,sticky='W')
    variable.grid(row=0, column=1,padx=2,pady=2)
    signe.grid(row=0,column=2,padx=2,pady=2)
    entree.grid(row=0,column=3,padx=2,pady=2)
    aide.grid(row=1,column=4,rowspan=2, padx=2, sticky='W')
    ok.grid(row=0,column=4,padx=2,pady=2)
    sinon.grid(row=2,rowspan=2,column=0,columnspan=2,padx=2,pady=2,sticky='W')
def tantque(evenement=None):
    rideau = Toplevel(fenetre)
    rideau.title("TANT QUE...")
    dimension(rideau,3,12,FALSE)
    center(rideau)
    """Sous fonction"""
    def bind(event):
        confirmer()
    def confirmer():
        recupvariable = spinvar.get()
        recupsigne = spinsigne.get()
        recupvaleur = box.get()
        zonefr.insert(END,"Tant que {} {} {} alors:\n".format(recupvariable,recupsigne,recupvaleur))
        zonepy.insert(END,"while {} {} {}:\n".format(recupvariable,recupsigne,recupvaleur))
        nligne()
        etat2()
        etat3()
        rideau.destroy()
    def verifier():
        recupvariable = spinvar.get()
        recupsigne = spinsigne.get()
        variableok = False
        signeok = False
        if recupvariable in varliste:
            variableok = True
        else:
            showerror("Erreur de variables","La variable que vous avez choisis n'existe pas\nVeuillez recommencer.")
        if recupsigne in signeliste:
            signeok = True
        else:
            showerror("Erreur de signes","Le signe que vous avez choisis n'existe pas.\nVeuillez recommencer.")
        if variableok is True and signeok is True:
            confirmer()
    def aide():
        tringle = Toplevel()
        tringle.title("TANT QUE...")
        dimension(tringle,4,5,FALSE)
        center(tringle)
        widgetdim(tringle)
        police = tkFont.Font(family="Helvetica",size=24,weight="bold")
        Label(tringle, text="TANT QUE...",fg="Red").grid(row=0,column=0,sticky=W)
        msg = Message(tringle,width=widgetlargeur-10,anchor='center',justify='left', text="Cette fonction permet à l'utilisateur d'imposer"
                                                        " une boucle à son programme.\n"
                                                        "Exemple:\n\tTant que 'b' < 30 alors\n\ton ajoute 2 à 'b' jusqu'a ce que "
                                                        "'b' soit \tsupérieur à 30")
        msg.grid(row=1, column=0,sticky=W)
    """Définition des variables"""
    spinvar = StringVar()
    spinsigne = StringVar()
    box = StringVar()
    variable = Spinbox(rideau,values=varliste,textvariable=spinvar,width=12)
    signe = Spinbox(rideau, values=signeliste, textvariable=spinsigne, width=5)
    entree = Entry(rideau, textvariable=box, width=12)
    aide = Button(rideau, text="Aide", command=aide)
    ok = Button(rideau,text="ok",command=verifier)
    """Position des variables"""
    Label(rideau,text="TANT QUE").grid(row=0,column=0,padx=2,pady=2,sticky='W')
    variable.grid(row=0, column=1,padx=2,pady=2)
    signe.grid(row=0,column=2,padx=2,pady=2)
    entree.grid(row=0,column=3,padx=2,pady=2)
    aide.grid(row=1,column=0,rowspan=2, padx=2, sticky='W')
    ok.grid(row=0,column=4,padx=2,pady=2)
def pour(evenement=None):
    rideau= Toplevel()
    rideau.title("POUR...")
    dimension(rideau,4.3,12,FALSE)
    center(rideau)
    """sous fonction"""
    def bind(event):
        confirmer()
    def confirmer():
        recupvaleur = box.get()
        recupvaleur2 = box2.get()
        recupvaleur2=int(recupvaleur2)+1#car par défaut python prend n-1, d'ou le +1
        print(recupvaleur, recupvaleur2)
        zonefr.insert(END,"Pour i allant de {} à {} alors:\n".format(recupvaleur, recupvaleur2))
        zonepy.insert(END,"for i in range({},{}):\n".format(recupvaleur,recupvaleur2))
        nligne()
        etat2()
        etat3()
        rideau.destroy()
    def verifier():
        recupvaleur = box.get()
        recupvaleur2 = box2.get()
        if len(recupvaleur) == 0 or len(recupvaleur2) == 0:
            showerror("Erreur de paramètres","Les paramètres sont incomplets\nVeuillez les compléter.")
        elif recupvaleur in varliste or recupvaleur2 in varliste:
            askokcancel("Êtes-vous sûre?", "Attention! Si la variable choisis en paramètre"+
                        " n'est pas un nombre de type entier 'int', votre programme est faussé.")
            confirmer()
        elif recupvaleur in nbstr or recupvaleur2 in nbstr:
            askokcancel("Êtes-vous sûre?", "Attention! Si la valeur choisis en paramètre"+
                        " n'est pas un nombre de type entier 'int', votre programme est faussé.")
            confirmer()
        else:
            showerror("Erreur de paramètres","Les paramètres sont incorrects\nVeuillez recommencer.")
    """Définition des variables"""
    spinvar = StringVar()
    box = StringVar()
    box2 = StringVar()
    entree = Entry(rideau, textvariable=box, width=5)
    entree2 = Entry(rideau, textvariable=box2, width=5)
    ok = Button(rideau,text="ok",command=verifier)
    """Position des variables"""
    Label(rideau,text="POUR i").grid(row=0,column=0,padx=2,pady=2,sticky='W')
    Label(rideau,text="ALLANT").grid(row=0,column=2,padx=2,pady=2)
    entree.grid(row=0,column=3,padx=2,pady=2)
    Label(rideau,text="à").grid(row=0,column=4,padx=3,pady=2)
    entree2.grid(row=0,column=5,padx=2,pady=2)
    ok.grid(row=0,column=6,padx=2,pady=2,sticky='E')
"""fonction commandes"""
def supprimer(evenement=None):
    rideau = Toplevel()
    rideau.title("Supprimer une ligne")
    dimension(rideau,6,11,FALSE)
    center(rideau)
    """sous fonction"""
    def confirmer():
        global nbligne
        n = float(box.get())
        m = float(nbligne)
        Text.delete(zonepy, index1=n, index2=n+1)
        Text.delete(zonefr, index1=n, index2=n+1)
        Text.delete(zoneligne, index1=m, index2=m+1)
        nbligne -= 1
    def bind(event):
        confirmer()
    box = IntVar()
    ligne = Entry(rideau,textvariable=box,width=5)
    ok = Button(rideau, text="Supprimer", command=confirmer)
    """realiser"""
    Label(rideau,text="Choisir la ligne").grid(row=0, column=0)
    ligne.grid(row=0,column=1,sticky=E)
    ok.grid(row=1, column=1)
def importer(evenement=None):
    rideau = Toplevel()
    rideau.title("Supprimer une ligne")
    dimension(rideau,4,11,FALSE)
    center(rideau)
    """sous fonction"""
    def bind(event):
        confirmer()
    def confirmer():
        recupimport = box.get()
        zonefr.insert(END, "On importe le module {}\n".format(recupimport))
        zonepy.insert(END, "import {}\n".format(recupimport))
        nligne()
        etat3()
        rideau.destroy()
    """variables tkinter permettant l'affichage graphique"""
    box = StringVar()
    entree = Entry(rideau,textvariable=box, width=20)
    ok = Button(rideau, text="Importer", command=confirmer)
    """Position des variables tkinter"""
    Label(rideau,text="Module à importer: ").grid(row=0,column=0)
    entree.grid(row=0,column=1)
    ok.grid(row=1,column=1,sticky='E')
def indenter(evenement=None):
    showinfo("Indentation","Indentation terminée")
    zonefr.insert(END,"     ")
    zonepy.insert(END,"     ")
"""Menu"""
menubar = Menu(fenetre)
menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label= "Ouvrir", command=ouvrir)
menu1.add_command(label= "Enregistrer", command=enregistrer)
menu1.add_command(label= "Exporter Ctrl+E", command=exporter)
menu1.add_separator()
menu1.add_command(label= "Quitter Ctrl+Q", command=quitter)
menubar.add_cascade(label= "Fichier", menu= menu1)
menu2 = Menu(menubar, tearoff=0)
menubar.add_cascade(label= "Aide", menu= menu2)
menu2.add_command(label= "Aide en ligne", command= alert)
menu2.add_command(label= "Documentation", command= documentation)
menu2.add_command(label= "A propos...", command=apropos)
fenetre.config(menu= menubar)
"""Zone commentaire"""
lbf1 = LabelFrame(fenetre, text= "Présentation du projet")
lbf1.configure(bg = "#cccccc")
lbf1.pack(side = TOP, expand= "no", fill= "both", anchor= "n", padx= 10, pady= 5)
zonepresentation= StringVar()
zonepresentation = Text(lbf1, height = 5)
zonepresentation.pack(expand= "yes", fill= "both")
"""Zone boites de texte"""
lbf2 = LabelFrame(fenetre)
lbf2.configure(bg = "#cccccc")
lbf2.pack(side = TOP, expand= "yes", fill= "both", anchor= "c", padx= 10, pady= 5)
scrollbar = Scrollbar(lbf2)
scrollbar2 = Scrollbar(lbf2)
scrollbar2.pack(side = RIGHT, fill = "y")
"""Définition des zones de textes"""
zonefr= Text(lbf2, yscrollcommand = scrollbar.set, bg = "white",borderwidth=0,relief=SUNKEN)
zonepy= Text(lbf2, yscrollcommand = scrollbar2.set,bg = "white",borderwidth=0,relief=SUNKEN)
zoneligne = Text(lbf2, bg = "gray", fg="black", width=1,borderwidth=0)
"""Bind des zones de textes - interdiction d'écrire à l'intérieur par l'utilisateur"""
zonefr.bind('<KeyPress>', lambda e: "break") #lambda est une mini-fonction, e un paramètre, "break" expression a faire
zonefr.bind('<Button-1>', lambda e: "break")
zonepy.bind('<Button-1>', lambda e: "break")
zonepy.bind('<KeyPress>', lambda e: "break") #lambda est une mini-fonction, e un paramètre, "break" expression a faire
zoneligne.bind('<KeyPress>', lambda e: "break")
zoneligne.bind('<Button-1>', lambda e: "break")
"""Position des zones de textes"""
zoneligne.pack(side = LEFT,expand= "yes", fill= "both", anchor= "w", padx= 2,)
zonefr.pack(side = LEFT, expand= "yes", fill= "both", anchor= "w", padx=2)
zonepy.pack(side = RIGHT, expand= "yes", fill= "both", anchor= "e", padx= 2)
scrollbar.pack(side = RIGHT, fill = "y")
scrollbar.config(command= zonefr.yview)
scrollbar2.config(command= zonepy.yview)
"""Conteneur Zone boutons + zone commandes"""
f7 = Frame(fenetre)
f7.configure(bg = "#cccccc")
f7.pack(side = TOP, expand= "no", fill= "both",anchor= "s")
"""Zone boutons"""
lbf3 = LabelFrame(f7, text= "Boutons")
lbf3.configure(bg = "#cccccc")
lbf3.pack(side = LEFT, expand= "yes", fill= "both", padx= 10, pady= 5)
"""définition des frames"""
f3 = Frame(lbf3)
f4 = Frame(lbf3)
f5 = Frame(lbf3)
f3.configure(bg = "#cccccc")
f4.configure(bg = "#cccccc")
f5.configure(bg = "#cccccc")
"""définition des boutons"""
b1 = Button(f3, text='Créer variable', command=creevariable)
b2 = Button(f3, text='Lire variable', command=lirevariable,state="disabled")
b3 = Button(f3, text='Affecter une valeur à', command=affecter,state="disabled")
b4 = Button(f4, text='Afficher variable', command=affichervar,state="disabled")
b5 = Button(f4, text='Afficher texte', command=affichertxt)
b6 = Button(f4, text='Afficher calcul', command=afficherclc)
b7 = Button(f5, text='POUR...DANS...', command=pour)
b8 = Button(f5, text='TANT QUE...', command= tantque)
b9 = Button(f5, text='SI...SINON...', command= sisinon)
"""position des boutons"""
b1.pack(expand= "yes", fill= "both", padx= 5, pady= 3)
b2.pack(expand= "yes", fill= "both", padx= 5, pady= 3)
b3.pack(expand= "yes", fill= "both", padx= 5, pady= 3)
b4.pack(expand= "yes", fill= "both", padx= 5, pady= 3)
b5.pack(expand= "yes", fill= "both", padx= 5, pady= 3)
b6.pack(expand= "yes", fill= "both", padx= 5, pady= 3)
b7.pack(expand= "yes", fill= "both", padx= 5, pady= 3)
b8.pack(expand= "yes", fill= "both", padx= 5, pady= 3)
b9.pack(expand= "yes", fill= "both", padx= 5, pady= 3)
"""bind des boutons"""
fenetre.bind("<Control-r>",creevariable)
fenetre.bind("<Control-t>",lirevariable)
fenetre.bind("<Control-y>",affecter)
fenetre.bind("<Control-u>",affichervar)
fenetre.bind("<Control-i>",affichertxt)
fenetre.bind("<Control-k>",afficherclc)
fenetre.bind("<Control-p>",pour)
fenetre.bind("<Control-d>",tantque)
fenetre.bind("<Control-f>",sisinon)
fenetre.bind("<Control-g>",importer)
fenetre.bind("<Control-h>",indenter)
fenetre.bind("<Control-j>",supprimer)
fenetre.bind("<Control-q>",quitter)
fenetre.bind("<Control-w>",quitter)
fenetre.bind("<Control-e>",exporter)
"""position des frames"""
f3.pack(side = LEFT, expand= "yes", fill= "both", padx= 2, pady= 2)
f4.pack(side = LEFT, expand= "yes", fill= "both", padx= 2, pady= 2)
f5.pack(side = LEFT, expand= "yes", fill= "both", padx= 2, pady= 2)
"""Zone commandes"""
lbf4 = LabelFrame(f7, text= "Commandes")
lbf4.configure(bg = "#cccccc")
lbf4.pack(side = RIGHT, expand= "yes", fill= "both", padx= 10, pady= 5)
"""Définition des boutons de commandes"""
b10 =Button(lbf4, text='Importer un module', command=importer)
b11 =Button(lbf4, text='Indenter une ligne', command=indenter,state="disabled")
b12 =Button(lbf4, text='Supprimer une ligne', command=supprimer,state="disabled")
"""position des boutons"""
b10.pack(expand= "yes", fill= "both", padx= 5, pady= 3)
b11.pack(expand= "yes", fill= "both", padx= 5, pady= 3)
b12.pack(expand= "yes", fill= "both", padx= 5, pady= 3)
#Fin zone commandes
fenetre.mainloop()