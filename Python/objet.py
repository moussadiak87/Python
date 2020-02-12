class Animal(): 
    #Ceci est la methode de construction de la classe animal. 
    def __init__(self):
    #attributs 
        self.age = 0 
        self.poids = 0 
        self.taille = 0 
        self.nombre_de_pattes = 0 

    #methodes
    def se_deplacer(self):
        print ("je me suis deplace")
        
    def se_nourrir(self):
        print ("je me suis nourris")


mon_animal = Animal() # variable de type "objet de classe Animal"
mon_autre_animal = Animal() 

print(mon_animal.taille)
mon_autre_animal.se_deplacer()















