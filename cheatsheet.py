"""
type de variable : 
numerique 
	int float 
alphanumerique 
	str
booleen 
	bool
"""
#declaration de variables
ma_var = ""
mon_autre_var = -0.0 
ma_derniere_var = False

# definition d'une fonction
def ma_fonction(longueur, largeur):
	perimetre = 2* (longueur + largeur)
	print (mon_autre_var)
	return [perimetre, perimetre ** 2]

#print (perimetre)

mon_perimetre = ma_fonction(4, 2)
# mon_perimetre = [perimetre, perimetre ** 2]
# mon_perimetre = [12, 144]

"martin;pierre;alléesdescoocielnlle;01-01-2000"
["martin", "pierre", "allés des coccinelles", "01-01-2000"]


class Ma_classe():
 	def __init__(self):
 		self.nom = "Cedric"
 		self.poids = "180"

 	def ma_methode(self, age):
 		limite = 18
 		if age > limite : #true 
 			resultat = True
 		else:
 			resutlat = False 
 		return resultat

#instantiation
mon_objet = Ma_classe()

# appel de la methode de l'objet
mon_objet.ma_methode(20)
print (mon_objet.nom) 
# reproduire cet appel de méthode pour un groupe de plusieurs valeurs.
# propriété d'un tableau : taille, type de données qu'il contient
#Creeer un tableau vide
mon_tableau = []

#creer un tableau plein
mon_tableau = [54,65,42,321,84,9687,6584,313,84,461,351,65,135,1356,1568,135,135,56143254]
#do while 
# ne se fait pas en python :-) 
#while 
# on ne connait pas le nombre d'itération
# on va devoir intervenir sur la conditions dans le corps de la boucle pour atteindre la conditions de sortie  
#for 
# On connait le nombre d'itération exacte 
# parce que la condition de sortie est fixé dans la declaration de la boucle

# for (i = 0; i < mon_tableau.length; i++):
# 	mon_objet.ma_methode(mon_tableau[i])



for (i=0; i<len(mon_tableau); i ++):


# range () n'inclut pas la borne superieur
for i in range(0, len(mon_tableau)):
	#instructions
	mon_affichage = mon_objet.ma_methode(mon_tableau[i])
	print (i, mon_affichage)

i = 0 
while (i < len(mon_tableau)) :
	# instructions 
	mon_affichage = mon_objet.ma_methode(mon_tableau[i])
	print (mon_affichage)
	# incrementation 
	i = i + 1 
	#i += 1 

mon_entrée_utilisateur = input()

# un import d'une bibliothèque 
import math 
ma_racine = math.sqrt(8)
ma_valeur = math.absval(-15)

from math import sqrt, absval, une_focntion_de_math
ma_racine = sqrt(8)
ma_valeur_absolue = absval(-15)
une_variable = une_focntion_de_math(1234)

from math import *
ma_racine = sqrt(8)
ma_valeur_absolue = absval(-15)
une_variable = une_focntion_de_math(1234)

