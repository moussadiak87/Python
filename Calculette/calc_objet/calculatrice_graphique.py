#import tkinter
from tkinter import Tk, Entry, Button

class Calculatrice_graphique():
    def __init__(self):
        self.fenetre = Tk(className = "une calculette")
        self.ecran = Entry(self.fenetre)
        self.pave_numerique = []
        self.symbole_operateur = ["=", "+", "-", "/", "*", "C"]
        self.pave_operateur = []
        
    def creer_pave_numerique(self):
        for i in range (0, 10):
            self.pave_numerique.append(Button(self.fenetre, text = i))
        self.pave_numerique.append(Button(self.fenetre, text = "."))

    def creer_pave_operateur(self):
        for i in range (0, len(self.symbole_operateur)):
            self.pave_operateur.append(Button(self.fenetre, text = self.symbole_operateur[i]))

    def agencer_elements(self):
        self.ecran.grid(row = 0, columnspan = 3, sticky="ew")
        for i in range (0, len(self.pave_numerique)):
            self.pave_numerique[i].grid(row = ((i-1)//3)+1, column = (i-1)%3, sticky = "ew")
            if i == 0: 
                self.pave_numerique[0].grid(row = 4, column = 1, sticky = 'ew')

        for i in range (0, len(self.pave_operateur)):
            self.pave_operateur[i].grid(row = i , column = 3, sticky = "ew")

    def associer_commande_pave_numerique(self):
        for i in range (0, len(self.pave_numerique)):
            self.pave_numerique[i].configure(command = lambda valeur = i : afficher(valeur))
        self.pave_numerique[-1].configure(command = lambda : afficher("."))


def afficher(nombre):
    print(nombre)