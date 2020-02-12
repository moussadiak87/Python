import algebre as alg

class Calculette():
	def __init__(self):
		self.valeur = ""
		self.resultat = 0
		self.memoire = 0 
		self.operateur = ""
	
	def clear(self):
		self.valeur = ""
		self.resultat = 0
		self.memoire = 0
		self.operateur = ""

	def operer(self):
		print ('m', self.memoire)
		print ('o', self.operateur)
		print ('v', self.valeur)
		if self.operateur == "+":
			self.resultat = alg.addition(int(self.memoire), int(self.valeur))
		elif self.operateur == "-":
			self.resultat = alg.soustraction(int(self.memoire), int(self.valeur))
		elif self.operateur == "*":
			self.resultat = alg.multiplication(int(self.memoire), int(self.valeur))
		elif self.operateur == "/":
			self.resultat = alg.division(int(self.memoire), int(self.valeur))
		elif self.operateur == "=":
			self.valeur = 0
		elif self.operateur == "C":
			self.clear()
		print ('r', self.resultat)
		self.valeur = ""
		self.memoire = self.resultat
		return self.resultat
