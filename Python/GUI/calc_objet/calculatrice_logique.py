class Calculatrice_logique():
    def __init__(self):
        self.valeur1 = 0
        self.valeur2 = 0 
        self.operateur = ""
        self.resultat = 0 

    def set_valeur1(self, valeur):
        # modifier la valeur de l'attribut valeur1 avec la valeur passé en paramètres
        self.valeur1 = valeur
        print (self.valeur1)
    
    def set_operateur(self, operateur):
        self.operateur = operateur
        print (self.operateur)
        self.valeur2 = self.valeur1
        self.valeur1 = 0

    def operer(self):         
        print(self.valeur2)
        print(self.operateur)
        print(self.valeur1) 

        if self.operateur == "+": 
            self.resultat = self.valeur2 + self.valeur1
        elif self.operateur == "-":
            self.resultat = self.valeur2 - self.valeur1
        elif self.operateur == "*":
            self.resultat = self.valeur2 * self.valeur1
        elif self.operateur == "/":
            self.resultat = self.valeur2 / self.valeur1
        

print (__name__)
"""
prendre les valeur qu'on rentre et afficher memoriser'
chronologique 
entrer une premiere valeur 
entrer un operateur
entrer une deuxieme valeur 
demander le resultat
exemple : 5 * 89 = 

valeur1, valeur2, operateur, resultat
ecrire 'saisir une valeur '
lire valeur1
ecrire 'saisir un operateur'
lire operateur
ecrire 'saisir une 2nde valeur'
lire valeur2
ecrire valeur1 operateur valeur2 (sous entendu: le resultat de l'operation en question)
"""

