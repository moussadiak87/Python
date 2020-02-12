import tkinter as tkr
from arithmetique import Calculette
"""
Construction de l'IHM de une_calculette : 
1- Creation des widgets (instanciation d'objet de classe [classe correspondante])
2- Afichage des widgets (utilisation du layout manager grid pour disposer les widget comme illustré lors du maquettage  )

1 - 
On crée une fenetre 
Sur cette fenetre, on ajoute le éléments du zoning (1 ecran, 1 pavé numérique, 1 pavé opérateurs, 1 zone instruction)
Dans le pavé numérique, on crée un tableau qui contient 11 bouttons (valeur de 0 à 9 et le boutton pour le symbole decimal). 
Dans le pavé operateurs,on crée un tableau qui contient 4 bouttons pour les symboles des opérations arithmetiques de base. 

2 - 
Gestion de l'affichage : 
Tout les éléments créé à la construction sont affiché dans leur container respectif avec une gestion de la disposition par grille (grid layout management)
On utilisera l'algorithmique pour déterminer les coordonnées correctes. 
"""

# def afficher (valeur, ecran):
# 	affichage = ecran.get()
# 	ecran.delete(0, 'end')
# 	affichage = affichage + str(valeur) 
# 	ecran.insert(0, affichage)

class Ihm_calculette():
	def __init__(self, calculette):
		self.calculette = calculette
		self.fenetre = tkr.Tk(className = "ma calculette")
		self.ecran = tkr.Entry(self.fenetre)
		self.ecran.insert(0, 0)
		self.boutons_numeriques = [tkr.Button(self.fenetre, text = str(nombre), command = lambda x = nombre : self.empiler_valeur(x)) for nombre in range (0,10)] 	# wireframe 
		self.boutons_numeriques.append(tkr.Button(self.fenetre, text = ".", command = lambda x = '.': self.empiler_valeur(x)))
		self.operateurs = ["=", "+", "-", "*", "/", "C"]
		self.bouttons_operateurs = [tkr.Button(self.fenetre, text = signe, command = lambda x = signe : self.operation(x)) for signe in self.operateurs]

	def lay_elements(self): #invoquer 
		self.ecran.grid(row = 0, column = 0, columnspan = 4)
		for nombre in range(len(self.boutons_numeriques)):
			if (nombre != 0): 
				self.boutons_numeriques[nombre].grid(row = ((nombre -1) // 3) + 1, column = (nombre - 1) % 3, sticky = "ew")
			else :
				self.boutons_numeriques[nombre].grid(row = 4, column = 1, sticky = "ew", columnspan = 2)

		for nombre in range (len(self.bouttons_operateurs)):
			if (nombre != 0): 
				self.bouttons_operateurs[nombre].grid(row = nombre, column = 3, sticky = "ew")
			else : 
				self.bouttons_operateurs[nombre].grid(row = len(self.bouttons_operateurs) - 1, column = 0, columnspan = 3, sticky = "ew")
		self.fenetre.mainloop()

	def operation (self, signe):
		self.print_status()
		self.ecran.delete(0, 'end')
		if signe == "=":
			self.ecran.insert(0, str(self.calculette.operer()))
			self.calculette.memoire = self.calculette.resultat
		else :
			self.calculette.operateur = signe
			self.calculette.memoire = self.calculette.valeur
			self.calculette.valeur = ""
			# self.ecran.insert(0, str(self.calculette.operer()))
			self.print_status()

	def print_status(self):
		print ('m', self.calculette.memoire)
		print ('o', self.calculette.operateur)
		print ('v', self.calculette.valeur)
		print ('r', self.calculette.resultat)

	def empiler_valeur(self, valeur):
		# self.ecran.insert(len(self.ecran.get()), valeur)
		self.calculette.valeur += str(valeur)
		print (self.calculette.valeur)
		self.ecran.delete(0, "end")
		self.ecran.insert(0, self.calculette.valeur)
		# print (self.calculette.valeur)
		# self.calculette.valeur = self.ecran.get()

	
	

if __name__ == '__main__':
	ma_calc = Ihm_calculette()
	ma_calc.lay_elements()