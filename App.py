from tkinter import *
from tkinter import ttk
from CadPerfil import * 

class App:
    def __init__(self):
        self.root = j
        self.tela()
        self.frame()
        self.PText()
        j.mainloop()


    def tela(self):
        self.root.title("Detran")
        
    def frame(self):
        self.mF = ttk.Frame(self.root, padding="12 12 12 12")
        self.mF.grid(column=0,row=0, sticky=(N, W, E, S))
        self.mF.columnconfigure(0, weight=1)
        self.mF.rowconfigure(0, weight=1)
        for child in self.mF.winfo_children(): 
            child.grid_configure(padx=5, pady=5)
        

    def PText(self): #Texto principal
        #self.mF.bind("<Return>", MudaJanela)
        welcomeText = Label(self.mF, text="Bem vindo ao sistema do Detran!\nAperte o botão abaixo para começar seu cadestro").grid(column=0, row=0, sticky=(N,E,S,W))
        login = Button(self.mF,text="LogIn",command=self.entraCadPerfil).grid(column=0,row=1,sticky=(N,E,S,W))

    def entraCadPerfil(self): #Botão para a tela de cadastro do perfil
        self.hide()
        self.subFrame = CadPerfil(self.mF)
    
    def hide(self): #esconde a tela principal
        self.root.withdraw()

    def show(self): #mostra a tela principal
        self.root.update()
        self.root.deiconify()
       
###################################################3
j = Tk() #Sempre a primeira linha de código
App()

