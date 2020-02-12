"""
nom : calcul_perimetre_rectangle
role : calculer le permietre d'un rectangle 
entrée : longueur, largeur
sorties:  perimetre 
variables longueur, largeur, perimetre
Debut 
perimetre <= (longeur + largeur) * 2 
retourne perimetre 
"""

def calcul_perimetre_rectangle(longueur, largeur):
    perimetre = (longueur + largeur) * 2
    return perimetre

"""
nom : calcul_perimetre_cercle
role 
entrée : rayon 
sortie : perimetre
variables :  rayon, perimetre en numerique 
Debut
perimetre <=  2 * rayon * 3.14
retourne perimetre 
"""
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


















