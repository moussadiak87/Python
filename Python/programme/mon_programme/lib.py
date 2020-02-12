un_age = 42 

def calcul_perimetre_rectangle(longueur, largeur):
    perimetre = (longueur + largeur) * 2
    return perimetre

def calcul_perimetre_cercle(rayon):
    perimetre = 2 * rayon * 3.14
    return perimetre

def determiner_signe_arithmetique(nombre):
    if nombre > 0 :
        print ("votre nombre " + str(nombre) + " est positif")
        return ("positif")
    else : 
        if nombre == 0 :
            print ("votre nombre", nombre, "est egale à 0")
        else : 
            print("votre nombre", nombre, "est negatif")

def affecter_categorie(age):
    liste_categorie = ["poussin", "pupille", "minime", "cadet", "aucune"]
    if age >= 6 : 
        if age <= 7:
            print ("Tu es dans la categorie", liste_categorie[0])
            return liste_categorie[0]
        elif age <= 9:
            print("Tu es dans la categorie", liste_categorie[1]+".")
            print("Tu es dans la categorie " + liste_categorie[1]+ ".")
            return liste_categorie[1]
        elif age <= 11:
            print ("tu es dans la categorie", liste_categorie[2])
            return liste_categorie[2]
        else:
            print ("tu es dans la categorie", liste_categorie[3])
            return liste_categorie[3]
    else : 
        print ("tu es dans", liste_categorie[4], "categorie.")
        return liste_categorie [4]

class Animal(): 
    #Ceci est la methode de construction de la classe animal. 
    def __init__(self):
    #attributs 
        self.age = 50
        self.poids = 0 
        self.taille = 0 
        self.nombre_de_pattes = 0 

    #methodes
    def se_deplacer(self):
        print ("je me suis deplace")
        
    def se_nourrir(self):
        print ("je me suis nourris")













