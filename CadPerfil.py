from tkinter import *
from tkinter import ttk


class CadPerfil(Toplevel):
    def __init__(self,original):
        self.principal = original
        Toplevel.__init__(self)
        self.frame()
        self.PText()
    
    def frame(self):
        self.mF2 = ttk.Frame(self, padding="12 12 12 12")
        self.mF2.grid(column=0,row=0, sticky=(N, W, E, S))
        self.mF2.columnconfigure(0, weight=1)
        self.mF2.rowconfigure(0, weight=1)
        for child in self.mF2.winfo_children(): 
            child.grid_configure(padx=5, pady=5)
        
    def PText(self): #Texto principal
        #self.mF.bind("<Return>", MudaJanela)
        welcomeText = Label(self.mF2, text="Cadastro Pessoa").grid(column=0, row=0, sticky=(W,E))
        Nome = Label(self.mF2, text="Insira seu nome").grid(column=0, row=1, sticky=(W,E))
        CPF = Label(self.mF2, text="Insira seu CPF").grid(column=0, row=2, sticky=(W,E))
        rg = Label(self.mF2, text="Insira seu RG").grid(column=0, row=3, sticky=(W,E))
        dt_nasc = Label(self.mF2, text="Insira sua data de nascimento").grid(column=0, row=4, sticky=(W,E))
        genero = Label(self.mF2, text="Insira seu gênero").grid(column=0, row=5, sticky=(W,E))
        login = Button(self.mF2,text="Terminar Cadastro").grid(column=0,row=10,sticky=(W,E))

    def cad(self,nome,cpf,rg,dt_nasc,genero):
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.dt_nasc = dt_nasc
        self.genero = genero

    def onClose(self):
        self.destroy()
        self.principal.show()

