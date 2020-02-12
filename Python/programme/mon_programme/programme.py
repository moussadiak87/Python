from lib import affecter_categorie
print ("entrez un age") 
age = int(input())
ma_categorie = affecter_categorie(age)
print ("votre enfant est en "+ ma_categorie)

'''import lib
print ("entrez un age") 
age = int(input())
ma_categorie = lib.affecter_categorie(age)
print ("votre enfant est en "+ ma_categorie)
'''

Ennoncé => reflexion => algo => reflexion => algo v2 => code => utilisation => reflexion => algo V3 => code v2=> utilisation => algo ...

import lib 
ma_categorie = lib.affecter_categorie(lib.un_age)
