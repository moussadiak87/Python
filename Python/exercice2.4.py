prix_hors_taxe = 0
tva = 0
prix_ttc= 0
nombre_article = 0
article = ""
article = "livre"

print ("Entrez le nombre d'article")
nombre_article = float(input()) #operation de lecture => stockage d'une valeur fournit parl'utilisateur au clavier dans une variable
print ("Entrez le prix hors taxe")
prix_hors_taxe = float(input())
print ("Entrez le taux de TVA entre 0 et 1")
tva = float(input())
prix_ttc = nombre_article * prix_hors_taxe * (1 + tva)
print ("Le prix total est de " + str(prix_ttc) + " $ ttc.")
