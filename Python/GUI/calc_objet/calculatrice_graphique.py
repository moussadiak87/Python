#import tkinter
from tkinter import Tk, Entry, Button

class Calculatrice_graphique():
    def __init__(self, calc_logique):
        self.logique = calc_logique
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
            self.pave_numerique[i].configure(command = lambda valeur = i : self.empiler_valeur(valeur))
        self.pave_numerique[-1].configure(command = lambda : self.empiler_valeur("."))
    
    def empiler_valeur(self, valeur):
        tampon = self.ecran.get() + str(valeur)
        self.ecran.delete(0, "end")
        self.logique.set_valeur1(float(tampon))
        self.ecran.insert(0, tampon)

    def associer_commande_pave_operateur(self): 
        # parcourir le tableau qui représente notre pavé operateur
        # avec une boucle
        # pour chaque tour de boucle: 
            # on va regarder l'élément indexé à la valeur de notre compteur
            # on va appeler la methode configure de l'objet de classe Button pour parametrer une commande associée à chacun des éléments
            # on attribue une commande en donnant à l'option command une valeur qui est une adresse mémoire.   
            #
            # Pour pouvoir passer des paramètres au traitement associé à la commande, on utilise une fonction anonyme A.K.A. une lambda
            #Cette lambda doit stocker le symbole de l'operateur dans l'attribut "logique" de notre objet graphique (plus précisement, dnas l'attribut operateur de l'attribut logique de notre objet graphique) 


        for i in range (0, len(self.pave_operateur)):
            self.pave_operateur[i].configure(command = lambda parametre_operateur =  self.symbole_operateur[i] : [self.logique.set_operateur(parametre_operateur), self.ecran.delete(0, "end")])
        self.pave_operateur[0].configure(command = self.afficher_resultat)
        

    def afficher_resultat(self): 
        self.ecran.delete(0, "end")
        self.logique.operer()
        self.ecran.insert(0, self.logique.resultat)

print (__name__)

if __name__ == "__main__":
    ma_variable = 42 
    print (ma_variable)








    


